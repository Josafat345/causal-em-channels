import numpy as np
import pytest
from scipy.integrate import cumulative_trapezoid

from causal_em.lorentz import LorentzParameters, integrate_trajectory


@pytest.mark.parametrize(
    "field,value",
    [
        ("damping_ratio", -0.1),
        ("modulation_depth", 1.0),
        ("modulation_depth", -1.0),
        ("modulation_ratio", 0.0),
    ],
)
def test_invalid_parameters_are_rejected(field: str, value: float) -> None:
    kwargs = {field: value}
    with pytest.raises(ValueError):
        LorentzParameters(**kwargs)


def test_energy_balance_converges() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.03,
        modulation_depth=0.25,
        modulation_ratio=1.6,
        phase=0.2,
    )
    trajectory = integrate_trajectory(
        parameters,
        initial_state=(0.7, -0.2),
        periods=8,
        samples_per_period=800,
    )
    accumulated_power = cumulative_trapezoid(
        trajectory.energy_rate, trajectory.tau, initial=0.0
    )
    residual = trajectory.energy - trajectory.energy[0] - accumulated_power
    scale = max(float(np.max(np.abs(trajectory.energy))), 1.0)
    assert np.max(np.abs(residual)) / scale < 2e-6


def test_augmented_energy_balance_is_satisfied_at_solver_tolerance() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.03,
        modulation_depth=0.25,
        modulation_ratio=1.6,
        phase=0.2,
    )
    trajectory = integrate_trajectory(
        parameters,
        initial_state=(0.7, -0.2),
        periods=8,
        samples_per_period=40,
    )
    scale = max(float(np.max(np.abs(trajectory.energy))), 1.0)
    assert np.max(np.abs(trajectory.energy_balance_residual)) / scale < 2e-9


def test_unforced_unmodulated_damped_energy_is_monotone() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.08,
        modulation_depth=0.0,
        modulation_ratio=1.0,
    )
    trajectory = integrate_trajectory(parameters, periods=5, samples_per_period=200)
    assert np.max(np.diff(trajectory.energy)) <= 2e-11
