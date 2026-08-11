from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = (ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")))
GITHUB_REJECTED_MACROS = (r"\operatorname",)
PROTECTED_INLINE_MATH = re.compile(r"\$`[^`]*`\$")
INLINE_CODE = re.compile(r"`[^`]*`")
INLINE_MATH = re.compile(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$")
COMMONMARK_SENSITIVE_LATEX_ESCAPE = re.compile(
    r'''\\[!"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~]'''
)


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


def test_display_math_uses_github_safe_fences() -> None:
    failures: list[str] = []

    for path in MARKDOWN_FILES:
        inside_fence = False
        fence_language = ""
        fence_opened_at = 0
        math_has_content = False

        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1
        ):
            stripped = line.lstrip()
            if stripped.startswith("```"):
                if not inside_fence:
                    inside_fence = True
                    fence_language = stripped[3:].strip()
                    fence_opened_at = line_number
                    math_has_content = False
                else:
                    if fence_language == "math" and not math_has_content:
                        failures.append(
                            f"{_relative(path)}:{fence_opened_at}: bloque math vacío"
                        )
                    inside_fence = False
                    fence_language = ""
                continue

            if not inside_fence and "$$" in line:
                failures.append(
                    f"{_relative(path)}:{line_number}: use ```math en vez de $$"
                )
            elif inside_fence and fence_language == "math":
                if "$$" in line:
                    failures.append(
                        f"{_relative(path)}:{line_number}: $$ dentro de bloque math"
                    )
                math_has_content = math_has_content or bool(line.strip())

        if inside_fence:
            failures.append(
                f"{_relative(path)}:{fence_opened_at}: bloque ``` sin cierre"
            )

    assert not failures, (
        "Bloques matemáticos incompatibles con GitHub:\n" + "\n".join(failures)
    )


def test_inline_math_protects_commonmark_sensitive_latex() -> None:
    failures: list[str] = []

    for path in MARKDOWN_FILES:
        inside_fence = False
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1
        ):
            if line.lstrip().startswith("```"):
                inside_fence = not inside_fence
                continue
            if inside_fence:
                continue

            unprotected = PROTECTED_INLINE_MATH.sub("", line)
            unprotected = INLINE_CODE.sub("", unprotected)
            for match in INLINE_MATH.finditer(unprotected):
                escape = COMMONMARK_SENSITIVE_LATEX_ESCAPE.search(match.group(1))
                if escape:
                    failures.append(
                        f"{_relative(path)}:{line_number}: {escape.group()} debe usar "
                        "$`...`$"
                    )

    assert not failures, (
        "GitHub consume escapes LaTeX dentro de matemática inline sin proteger:\n"
        + "\n".join(failures)
    )


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
