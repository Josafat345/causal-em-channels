"""Oscilador de Lorentz adimensional con parametros periodicos."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.integrate import solve_ivp

Forcing = Callable[[float], float]


@dataclass(frozen=True, slots=True)
class LorentzParameters:
    """Parametros adimensionales del oscilador de Lorentz periodico.

    La ecuacion es

        p'' + 2*zeta*p' + (1 + m*cos(nu*tau + phase))*p = f(tau).
    """

    damping_ratio: float = 0.02
    modulation_depth: float = 0.20
    modulation_ratio: float = 2.0
    phase: float = 0.0

    def __post_init__(self) -> None:
        values = (
            self.damping_ratio,
            self.modulation_depth,
            self.modulation_ratio,
            self.phase,
        )
        if not all(np.isfinite(value) for value in values):
            raise ValueError("Todos los parametros deben ser finitos.")
        if self.damping_ratio < 0:
            raise ValueError("damping_ratio debe ser no negativo.")
        if abs(self.modulation_depth) >= 1:
            raise ValueError("El prototipo requiere abs(modulation_depth) < 1.")
        if self.modulation_ratio <= 0:
            raise ValueError("modulation_ratio debe ser positivo.")

    @property
    def period(self) -> float:
        """Periodo adimensional de modulacion."""

        return 2.0 * np.pi / self.modulation_ratio

    def stiffness(self, tau: ArrayLike) -> float | NDArray[np.float64]:
        """Coeficiente periodico que multiplica a la polarizacion."""

        value = 1.0 + self.modulation_depth * np.cos(
            self.modulation_ratio * np.asarray(tau) + self.phase
        )
        return float(value) if np.ndim(value) == 0 else value

    def stiffness_derivative(self, tau: ArrayLike) -> float | NDArray[np.float64]:
        """Derivada de la rigidez respecto del tiempo adimensional."""

        value = -self.modulation_depth * self.modulation_ratio * np.sin(
            self.modulation_ratio * np.asarray(tau) + self.phase
        )
        return float(value) if np.ndim(value) == 0 else value

    def state_matrix(self, tau: float) -> NDArray[np.float64]:
        """Matriz A(tau) del sistema homogeneo x'=A(tau)x."""

        return np.array(
            [[0.0, 1.0], [-self.stiffness(tau), -2.0 * self.damping_ratio]],
            dtype=float,
        )


@dataclass(frozen=True, slots=True)
class Trajectory:
    """Trayectoria numerica y terminos de su balance energetico."""

    tau: NDArray[np.float64]
    state: NDArray[np.float64]
    energy: NDArray[np.float64]
    dissipation_power: NDArray[np.float64]
    modulation_power: NDArray[np.float64]
    input_power: NDArray[np.float64]
    dissipation_work: NDArray[np.float64]
    modulation_work: NDArray[np.float64]
    input_work: NDArray[np.float64]
    nfev: int

    @property
    def energy_rate(self) -> NDArray[np.float64]:
        return self.dissipation_power + self.modulation_power + self.input_power

    @property
    def accumulated_work(self) -> NDArray[np.float64]:
        """Trabajo neto acumulado de los tres puertos energeticos."""

        return self.dissipation_work + self.modulation_work + self.input_work

    @property
    def energy_balance_residual(self) -> NDArray[np.float64]:
        """Residuo de E(t)-E(0)=W_dis+W_mod+W_in."""

        return self.energy - self.energy[0] - self.accumulated_work


def integrate_trajectory(
    parameters: LorentzParameters,
    initial_state: ArrayLike = (1.0, 0.0),
    *,
    periods: float = 20.0,
    samples_per_period: int = 200,
    forcing: Forcing | None = None,
    rtol: float = 1e-10,
    atol: float = 1e-12,
    method: str = "DOP853",
) -> Trajectory:
    """Integra estado y trabajos acumulados del balance de energia."""

    if periods <= 0:
        raise ValueError("periods debe ser positivo.")
    if samples_per_period < 8:
        raise ValueError("samples_per_period debe ser al menos 8.")

    x0 = np.asarray(initial_state, dtype=float)
    if x0.shape != (2,) or not np.all(np.isfinite(x0)):
        raise ValueError("initial_state debe ser un vector finito de longitud 2.")

    drive = forcing if forcing is not None else (lambda _tau: 0.0)
    final_tau = periods * parameters.period
    sample_count = int(np.ceil(periods * samples_per_period)) + 1
    tau = np.linspace(0.0, final_tau, sample_count)

    def rhs(current_tau: float, augmented: NDArray[np.float64]) -> NDArray[np.float64]:
        p, velocity = augmented[:2]
        force = float(drive(current_tau))
        stiffness = float(parameters.stiffness(current_tau))
        stiffness_rate = float(parameters.stiffness_derivative(current_tau))
        dissipation_power = -2.0 * parameters.damping_ratio * velocity**2
        modulation_power = 0.5 * stiffness_rate * p**2
        input_power = velocity * force
        return np.array(
            [
                velocity,
                -stiffness * p - 2.0 * parameters.damping_ratio * velocity + force,
                dissipation_power,
                modulation_power,
                input_power,
            ],
            dtype=float,
        )

    solution = solve_ivp(
        rhs,
        (0.0, final_tau),
        np.concatenate((x0, np.zeros(3, dtype=float))),
        t_eval=tau,
        method=method,
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise RuntimeError(f"La integracion fallo: {solution.message}")

    p = solution.y[0]
    velocity = solution.y[1]
    stiffness = np.asarray(parameters.stiffness(tau))
    stiffness_rate = np.asarray(parameters.stiffness_derivative(tau))
    force = np.fromiter((float(drive(value)) for value in tau), dtype=float, count=len(tau))

    energy = 0.5 * (velocity**2 + stiffness * p**2)
    dissipation_power = -2.0 * parameters.damping_ratio * velocity**2
    modulation_power = 0.5 * stiffness_rate * p**2
    input_power = velocity * force

    return Trajectory(
        tau=tau,
        state=solution.y[:2],
        energy=energy,
        dissipation_power=dissipation_power,
        modulation_power=modulation_power,
        input_power=input_power,
        dissipation_work=solution.y[2],
        modulation_work=solution.y[3],
        input_work=solution.y[4],
        nfev=solution.nfev,
    )
