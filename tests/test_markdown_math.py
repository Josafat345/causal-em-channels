from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = (ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")))
GITHUB_REJECTED_MACROS = (r"\operatorname",)


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def test_markdown_avoids_github_rejected_math_macros() -> None:
    failures: list[str] = []
    for path in MARKDOWN_FILES:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for macro in GITHUB_REJECTED_MACROS:
                if macro in line:
                    failures.append(f"{_relative(path)}:{line_number}: {macro}")

    assert not failures, "GitHub rechazará estos macros LaTeX:\n" + "\n".join(failures)


def test_markdown_math_delimiters_are_balanced() -> None:
    failures: list[str] = []
    for path in MARKDOWN_FILES:
        text = path.read_text(encoding="utf-8")
        if text.count("$$") % 2:
            failures.append(f"{_relative(path)}: número impar de delimitadores $$")

        inside_fence = False
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                inside_fence = not inside_fence
                continue
            if inside_fence:
                continue
            without_display = line.replace("$$", "")
            without_escaped_dollars = without_display.replace(r"\$", "")
            if without_escaped_dollars.count("$") % 2:
                failures.append(
                    f"{_relative(path)}:{line_number}: delimitador $ sin pareja"
                )

    assert not failures, "Delimitadores matemáticos desbalanceados:\n" + "\n".join(failures)


def test_markdown_latex_environments_are_nested_and_balanced() -> None:
    token_pattern = re.compile(r"\\(begin|end)\{([^{}]+)\}")
    failures: list[str] = []

    for path in MARKDOWN_FILES:
        stack: list[tuple[str, int]] = []
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for action, environment in token_pattern.findall(line):
                if action == "begin":
                    stack.append((environment, line_number))
                elif not stack:
                    failures.append(
                        f"{_relative(path)}:{line_number}: \\end{{{environment}}} sin inicio"
                    )
                else:
                    opened, opened_line = stack.pop()
                    if opened != environment:
                        failures.append(
                            f"{_relative(path)}:{line_number}: se cerró {environment}, "
                            f"pero {opened} comenzó en la línea {opened_line}"
                        )

        failures.extend(
            f"{_relative(path)}:{line_number}: \\begin{{{environment}}} sin cierre"
            for environment, line_number in stack
        )

    assert not failures, "Entornos LaTeX desbalanceados:\n" + "\n".join(failures)
