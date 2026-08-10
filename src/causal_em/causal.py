"""Propagadores y respuesta causal de dos tiempos del medio de Lorentz."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.integrate import solve_ivp

from .lorentz import LorentzParameters


@dataclass(frozen=True, slots=True)
class PropagatorResult:
    """Matriz de transicion U(tau, source_tau) de un intervalo causal."""

    matrix: NDArray[np.float64]
    source_tau: float
    observation_tau: float
    nfev: int
    rtol: float
    atol: float

    @property
    def duration(self) -> float:
        return self.observation_tau - self.source_tau


def integrate_propagator(
    parameters: LorentzParameters,
    source_tau: float,
    observation_tau: float,
    *,
    rtol: float = 1e-11,
    atol: float = 1e-13,
    method: str = "DOP853",
) -> PropagatorResult:
    """Integra U'=A(tau)U, U(source_tau, source_tau)=I."""

    if not np.isfinite(source_tau) or not np.isfinite(observation_tau):
        raise ValueError("Los tiempos deben ser finitos.")
    if observation_tau < source_tau:
        raise ValueError("observation_tau debe ser mayor o igual que source_tau.")
    if observation_tau == source_tau:
        return PropagatorResult(
            matrix=np.eye(2, dtype=float),
            source_tau=float(source_tau),
            observation_tau=float(observation_tau),
            nfev=0,
            rtol=rtol,
            atol=atol,
        )

    def rhs(tau: float, flattened: NDArray[np.float64]) -> NDArray[np.float64]:
        propagator = flattened.reshape(2, 2)
        return (parameters.state_matrix(tau) @ propagator).ravel()

    solution = solve_ivp(
        rhs,
        (source_tau, observation_tau),
        np.eye(2, dtype=float).ravel(),
        method=method,
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise RuntimeError(f"La integracion del propagador fallo: {solution.message}")

    return PropagatorResult(
        matrix=solution.y[:, -1].reshape(2, 2),
        source_tau=float(source_tau),
        observation_tau=float(observation_tau),
        nfev=solution.nfev,
        rtol=rtol,
        atol=atol,
    )


def causal_susceptibility(
    parameters: LorentzParameters,
    observation_tau: float,
    source_tau: float,
    *,
    rtol: float = 1e-11,
    atol: float = 1e-13,
) -> float:
    """Nucleo g(tau,s)=e_p^T U(tau,s)e_v H(tau-s)."""

    if not np.isfinite(source_tau) or not np.isfinite(observation_tau):
        raise ValueError("Los tiempos deben ser finitos.")
    if observation_tau <= source_tau:
        return 0.0
    propagator = integrate_propagator(
        parameters,
        source_tau,
        observation_tau,
        rtol=rtol,
        atol=atol,
    )
    return float(propagator.matrix[0, 1])


def causal_susceptibility_grid(
    parameters: LorentzParameters,
    observation_times: ArrayLike,
    source_times: ArrayLike,
    *,
    rtol: float = 2e-10,
    atol: float = 2e-12,
    method: str = "DOP853",
) -> NDArray[np.float64]:
    """Evalua el nucleo causal sobre una malla rectangular de dos tiempos."""

    observations = np.asarray(observation_times, dtype=float)
    sources = np.asarray(source_times, dtype=float)
    if observations.ndim != 1 or sources.ndim != 1:
        raise ValueError("observation_times y source_times deben ser vectores 1D.")
    if not np.all(np.isfinite(observations)) or not np.all(np.isfinite(sources)):
        raise ValueError("Todos los tiempos deben ser finitos.")

    kernel = np.zeros((observations.size, sources.size), dtype=float)
    impulse_state = np.array([0.0, 1.0])

    for column, source_tau in enumerate(sources):
        causal_mask = observations > source_tau
        if not np.any(causal_mask):
            continue
        final_tau = float(np.max(observations[causal_mask]))

        def rhs(tau: float, state: NDArray[np.float64]) -> NDArray[np.float64]:
            return parameters.state_matrix(tau) @ state

        solution = solve_ivp(
            rhs,
            (float(source_tau), final_tau),
            impulse_state,
            method=method,
            rtol=rtol,
            atol=atol,
            dense_output=True,
        )
        if not solution.success or solution.sol is None:
            raise RuntimeError(f"La integracion del nucleo causal fallo: {solution.message}")
        kernel[causal_mask, column] = solution.sol(observations[causal_mask])[0]

    return kernel


def analytic_stationary_susceptibility(
    parameters: LorentzParameters,
    observation_tau: ArrayLike,
    source_tau: ArrayLike,
) -> float | NDArray[np.float64]:
    """Funcion de Green exacta del oscilador estacionario adimensional."""

    if not np.isclose(parameters.modulation_depth, 0.0, atol=0.0):
        raise ValueError("La solucion analitica requiere modulation_depth=0.")
    delay = np.asarray(observation_tau, dtype=float) - np.asarray(source_tau, dtype=float)
    causal_delay = np.maximum(delay, 0.0)
    zeta = parameters.damping_ratio

    if zeta < 1.0:
        damped_frequency = np.sqrt(1.0 - zeta**2)
        response = (
            np.exp(-zeta * causal_delay)
            * np.sin(damped_frequency * causal_delay)
            / damped_frequency
        )
    elif np.isclose(zeta, 1.0):
        response = causal_delay * np.exp(-causal_delay)
    else:
        rate = np.sqrt(zeta**2 - 1.0)
        response = np.exp(-zeta * causal_delay) * np.sinh(rate * causal_delay) / rate

    response = np.where(delay > 0.0, response, 0.0)
    return float(response) if np.ndim(response) == 0 else response
