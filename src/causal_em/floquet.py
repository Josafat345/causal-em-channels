"""Calculo y diagnosticos de Floquet para el modelo de Lorentz."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm

from .causal import integrate_propagator
from .lorentz import LorentzParameters


@dataclass(frozen=True, slots=True)
class MonodromyResult:
    """Resultado de integrar la matriz fundamental durante un periodo."""

    matrix: NDArray[np.float64]
    period: float
    nfev: int
    rtol: float
    atol: float

    @property
    def determinant(self) -> float:
        return float(np.linalg.det(self.matrix))

    @property
    def multipliers(self) -> NDArray[np.complex128]:
        return floquet_multipliers(self.matrix)

    @property
    def growth_rates(self) -> NDArray[np.float64]:
        return np.log(np.abs(self.multipliers)) / self.period

    @property
    def max_growth_rate(self) -> float:
        return float(np.max(self.growth_rates))


def integrate_fundamental(
    parameters: LorentzParameters,
    *,
    rtol: float = 1e-11,
    atol: float = 1e-13,
    method: str = "DOP853",
) -> MonodromyResult:
    """Integra Phi'=A(tau)Phi, Phi(0)=I, durante un periodo."""

    propagator = integrate_propagator(
        parameters,
        0.0,
        parameters.period,
        rtol=rtol,
        atol=atol,
        method=method,
    )

    return MonodromyResult(
        matrix=propagator.matrix,
        period=parameters.period,
        nfev=propagator.nfev,
        rtol=rtol,
        atol=atol,
    )


def floquet_multipliers(monodromy: NDArray[np.float64]) -> NDArray[np.complex128]:
    """Autovalores de la monodromia, ordenados por modulo decreciente."""

    matrix = np.asarray(monodromy)
    if matrix.shape != (2, 2):
        raise ValueError("La monodromia debe tener forma (2, 2).")
    values = np.asarray(np.linalg.eigvals(matrix), dtype=np.complex128)
    return values[np.argsort(np.abs(values))[::-1]]


def floquet_exponents(
    monodromy: NDArray[np.float64], period: float
) -> NDArray[np.complex128]:
    """Exponentes de Floquet en la rama principal del logaritmo."""

    if period <= 0:
        raise ValueError("period debe ser positivo.")
    return np.log(floquet_multipliers(monodromy)) / period


def spectral_radius(monodromy: NDArray[np.float64]) -> float:
    """Radio espectral de la monodromia."""

    return float(np.max(np.abs(floquet_multipliers(monodromy))))


def liouville_determinant(parameters: LorentzParameters) -> float:
    """Determinante exacto de la monodromia segun Liouville."""

    return float(np.exp(-2.0 * parameters.damping_ratio * parameters.period))


def analytic_constant_monodromy(parameters: LorentzParameters) -> NDArray[np.float64]:
    """Monodromia exacta por exponencial matricial cuando m=0."""

    if not np.isclose(parameters.modulation_depth, 0.0, atol=0.0):
        raise ValueError("La solucion analitica implementada requiere modulation_depth=0.")
    return np.asarray(expm(parameters.state_matrix(0.0) * parameters.period), dtype=float)


def stability_scan(
    damping_ratio: float,
    modulation_depths: NDArray[np.float64],
    modulation_ratios: NDArray[np.float64],
    *,
    rtol: float = 2e-8,
    atol: float = 2e-10,
) -> NDArray[np.float64]:
    """Tasa maxima de crecimiento sobre una malla de parametros."""

    depths = np.asarray(modulation_depths, dtype=float)
    ratios = np.asarray(modulation_ratios, dtype=float)
    growth = np.empty((len(depths), len(ratios)), dtype=float)

    for row, depth in enumerate(depths):
        for column, ratio in enumerate(ratios):
            parameters = LorentzParameters(
                damping_ratio=damping_ratio,
                modulation_depth=float(depth),
                modulation_ratio=float(ratio),
            )
            growth[row, column] = integrate_fundamental(
                parameters, rtol=rtol, atol=atol
            ).max_growth_rate
    return growth
