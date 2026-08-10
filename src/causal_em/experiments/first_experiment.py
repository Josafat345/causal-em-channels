"""Primer experimento: monodromia, estabilidad y energia de Lorentz-Floquet."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from causal_em.causal import causal_susceptibility_grid
from causal_em.floquet import (
    floquet_exponents,
    integrate_fundamental,
    liouville_determinant,
    spectral_radius,
    stability_scan,
)
from causal_em.lorentz import LorentzParameters, integrate_trajectory


def _complex_record(value: complex) -> dict[str, float]:
    return {"real": float(value.real), "imag": float(value.imag), "abs": float(abs(value))}


def _energy_residual(trajectory) -> np.ndarray:
    return trajectory.energy_balance_residual


def run(args: argparse.Namespace) -> dict[str, object]:
    if args.kernel_points_per_period < 8:
        raise ValueError("kernel_points_per_period debe ser al menos 8.")

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    parameters = LorentzParameters(
        damping_ratio=args.damping_ratio,
        modulation_depth=args.modulation_depth,
        modulation_ratio=args.modulation_ratio,
        phase=args.phase,
    )
    monodromy = integrate_fundamental(parameters)
    multipliers = monodromy.multipliers
    exponents = floquet_exponents(monodromy.matrix, monodromy.period)
    trajectory = integrate_trajectory(
        parameters,
        initial_state=(1.0, 0.0),
        periods=args.periods,
        samples_per_period=args.samples_per_period,
    )

    residual = _energy_residual(trajectory)
    residual_scale = max(float(np.max(np.abs(trajectory.energy))), 1.0)
    normalized_residual = float(np.max(np.abs(residual)) / residual_scale)

    figure, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True, constrained_layout=True)
    axes[0].plot(
        trajectory.tau / parameters.period, trajectory.state[0], label=r"$p$"
    )
    axes[0].plot(
        trajectory.tau / parameters.period,
        trajectory.state[1],
        label=r"$p'$",
        alpha=0.8,
    )
    axes[0].set_ylabel("Estado")
    axes[0].legend()
    axes[0].grid(alpha=0.25)

    axes[1].semilogy(
        trajectory.tau / parameters.period,
        np.maximum(trajectory.energy, np.finfo(float).tiny),
    )
    axes[1].set_ylabel(r"Energía $\mathcal{E}$")
    axes[1].grid(alpha=0.25)

    axes[2].plot(
        trajectory.tau / parameters.period,
        trajectory.dissipation_power,
        label="Disipacion",
    )
    axes[2].plot(
        trajectory.tau / parameters.period,
        trajectory.modulation_power,
        label="Bombeo temporal",
        alpha=0.8,
    )
    axes[2].set_xlabel(r"Períodos de modulación $n=\tau/T$")
    axes[2].set_ylabel("Potencia")
    axes[2].legend()
    axes[2].grid(alpha=0.25)
    figure.suptitle("Oscilador de Lorentz periódico")
    figure.savefig(output / "trajectory_and_energy.png", dpi=180)
    plt.close(figure)

    kernel_points_per_period = args.kernel_points_per_period
    source_times = np.linspace(0.0, 2.0 * parameters.period, 2 * kernel_points_per_period + 1)
    observation_times = np.linspace(
        0.0, 3.0 * parameters.period, 3 * kernel_points_per_period + 1
    )
    causal_kernel = causal_susceptibility_grid(
        parameters, observation_times, source_times
    )
    kernel_limit = max(float(np.max(np.abs(causal_kernel))), np.finfo(float).eps)

    figure, axis = plt.subplots(figsize=(8.5, 6.2), constrained_layout=True)
    image = axis.pcolormesh(
        source_times / parameters.period,
        observation_times / parameters.period,
        causal_kernel,
        shading="auto",
        cmap="RdBu_r",
        vmin=-kernel_limit,
        vmax=kernel_limit,
    )
    diagonal = np.linspace(0.0, 2.0, 100)
    axis.plot(diagonal, diagonal, color="black", linewidth=1.0, linestyle="--")
    axis.set_xlabel(r"Tiempo fuente $s/T$")
    axis.set_ylabel(r"Tiempo de observación $\tau/T$")
    axis.set_title(r"Núcleo causal de dos tiempos $g(\tau,s)$")
    figure.colorbar(image, ax=axis, label=r"Susceptibilidad $g(\tau,s)$")
    figure.savefig(output / "causal_kernel.png", dpi=180)
    plt.close(figure)

    np.savez_compressed(
        output / "causal_kernel_data.npz",
        observation_times=observation_times,
        source_times=source_times,
        susceptibility=causal_kernel,
    )

    points = kernel_points_per_period
    base_block = causal_kernel[: 2 * points + 1, : points + 1]
    shifted_block = causal_kernel[points : 3 * points + 1, points : 2 * points + 1]
    periodicity_scale = max(float(np.max(np.abs(base_block))), 1.0)
    kernel_periodicity_residual = float(
        np.max(np.abs(base_block - shifted_block)) / periodicity_scale
    )

    if args.with_map:
        depths = np.linspace(0.0, args.map_max_depth, args.map_depth_points)
        ratios = np.linspace(args.map_min_ratio, args.map_max_ratio, args.map_ratio_points)
        growth = stability_scan(parameters.damping_ratio, depths, ratios)

        figure, axis = plt.subplots(figsize=(9, 5.5), constrained_layout=True)
        image = axis.pcolormesh(ratios, depths, growth, shading="auto", cmap="coolwarm")
        axis.contour(ratios, depths, growth, levels=[0.0], colors="black", linewidths=1.2)
        axis.plot(parameters.modulation_ratio, parameters.modulation_depth, "ko", ms=5)
        axis.set_xlabel(r"$\nu=\Omega_m/\omega_0$")
        axis.set_ylabel(r"Profundidad $m$")
        axis.set_title("Tasa máxima de crecimiento de Floquet")
        figure.colorbar(
            image,
            ax=axis,
            label=r"$g_{\max}=\max_i\log|\lambda_i|/T$",
        )
        figure.savefig(output / "stability_map.png", dpi=180)
        plt.close(figure)

        np.savez_compressed(
            output / "stability_map_data.npz",
            modulation_depths=depths,
            modulation_ratios=ratios,
            growth_rates=growth,
        )

    summary: dict[str, object] = {
        "parameters": {
            "damping_ratio": parameters.damping_ratio,
            "modulation_depth": parameters.modulation_depth,
            "modulation_ratio": parameters.modulation_ratio,
            "phase": parameters.phase,
            "period": parameters.period,
        },
        "monodromy": monodromy.matrix.tolist(),
        "multipliers": [_complex_record(value) for value in multipliers],
        "principal_exponents": [_complex_record(value) for value in exponents],
        "spectral_radius": spectral_radius(monodromy.matrix),
        "max_growth_rate": monodromy.max_growth_rate,
        "determinant_numeric": monodromy.determinant,
        "determinant_liouville": liouville_determinant(parameters),
        "determinant_absolute_error": abs(
            monodromy.determinant - liouville_determinant(parameters)
        ),
        "normalized_energy_balance_residual": normalized_residual,
        "causal_kernel_max_abs": kernel_limit,
        "causal_kernel_joint_periodicity_residual": kernel_periodicity_residual,
        "fundamental_nfev": monodromy.nfev,
        "trajectory_nfev": trajectory.nfev,
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="results/first_experiment")
    parser.add_argument("--damping-ratio", type=float, default=0.02)
    parser.add_argument("--modulation-depth", type=float, default=0.20)
    parser.add_argument("--modulation-ratio", type=float, default=2.0)
    parser.add_argument("--phase", type=float, default=0.0)
    parser.add_argument("--periods", type=float, default=30.0)
    parser.add_argument("--samples-per-period", type=int, default=200)
    parser.add_argument("--kernel-points-per-period", type=int, default=40)
    parser.add_argument("--with-map", action="store_true")
    parser.add_argument("--map-max-depth", type=float, default=0.60)
    parser.add_argument("--map-min-ratio", type=float, default=0.50)
    parser.add_argument("--map-max-ratio", type=float, default=3.00)
    parser.add_argument("--map-depth-points", type=int, default=25)
    parser.add_argument("--map-ratio-points", type=int, default=41)
    return parser


def main() -> None:
    summary = run(build_parser().parse_args())
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
