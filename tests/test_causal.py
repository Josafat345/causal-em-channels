import numpy as np

from causal_em.causal import (
    analytic_stationary_susceptibility,
    causal_susceptibility,
    causal_susceptibility_grid,
    integrate_propagator,
)
from causal_em.lorentz import LorentzParameters


def test_stationary_kernel_matches_exact_green_function() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.15,
        modulation_depth=0.0,
        modulation_ratio=1.3,
    )
    observations = np.array([0.0, 0.1, 0.3, 0.9, 1.7, 2.4])
    sources = np.array([0.1, 0.7])
    numeric = causal_susceptibility_grid(parameters, observations, sources)
    exact = analytic_stationary_susceptibility(
        parameters, observations[:, None], sources[None, :]
    )
    np.testing.assert_allclose(numeric, exact, rtol=3e-10, atol=2e-11)


def test_kernel_is_exactly_zero_before_the_source_time() -> None:
    parameters = LorentzParameters()
    assert causal_susceptibility(parameters, 0.4, 0.7) == 0.0
    assert causal_susceptibility(parameters, 0.7, 0.7) == 0.0


def test_propagator_composition_has_correct_temporal_order() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.04,
        modulation_depth=0.33,
        modulation_ratio=1.8,
        phase=0.2,
    )
    source = 0.13 * parameters.period
    middle = 0.61 * parameters.period
    observation = 1.42 * parameters.period
    complete = integrate_propagator(parameters, source, observation).matrix
    first = integrate_propagator(parameters, source, middle).matrix
    second = integrate_propagator(parameters, middle, observation).matrix
    np.testing.assert_allclose(complete, second @ first, rtol=3e-11, atol=3e-12)


def test_kernel_has_joint_periodicity() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.025,
        modulation_depth=0.37,
        modulation_ratio=1.91,
        phase=0.31,
    )
    source = 0.23 * parameters.period
    observation = 1.17 * parameters.period
    base = causal_susceptibility(parameters, observation, source)
    shifted = causal_susceptibility(
        parameters,
        observation + parameters.period,
        source + parameters.period,
    )
    assert np.isclose(base, shifted, rtol=3e-11, atol=3e-12)
