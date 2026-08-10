import numpy as np

from causal_em.floquet import (
    analytic_constant_monodromy,
    integrate_fundamental,
    liouville_determinant,
    spectral_radius,
)
from causal_em.lorentz import LorentzParameters


def test_unmodulated_monodromy_matches_matrix_exponential() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.07,
        modulation_depth=0.0,
        modulation_ratio=1.7,
    )
    numeric = integrate_fundamental(parameters)
    exact = analytic_constant_monodromy(parameters)
    np.testing.assert_allclose(numeric.matrix, exact, rtol=2e-11, atol=2e-12)


def test_lossless_quarter_period_has_exact_rotation() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.0,
        modulation_depth=0.0,
        modulation_ratio=4.0,
    )
    result = integrate_fundamental(parameters)
    expected = np.array([[0.0, 1.0], [-1.0, 0.0]])
    np.testing.assert_allclose(result.matrix, expected, rtol=2e-11, atol=2e-12)


def test_liouville_identity_with_modulation() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.035,
        modulation_depth=0.45,
        modulation_ratio=1.83,
        phase=0.37,
    )
    result = integrate_fundamental(parameters)
    assert np.isclose(result.determinant, liouville_determinant(parameters), rtol=2e-10)


def test_undamped_monodromy_has_unit_determinant() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.0,
        modulation_depth=0.35,
        modulation_ratio=2.4,
    )
    result = integrate_fundamental(parameters)
    assert np.isclose(result.determinant, 1.0, rtol=2e-10, atol=2e-11)


def test_parametric_resonance_is_detected() -> None:
    parameters = LorentzParameters(
        damping_ratio=0.005,
        modulation_depth=0.20,
        modulation_ratio=2.0,
    )
    result = integrate_fundamental(parameters)
    assert spectral_radius(result.matrix) > 1.05
    assert result.max_growth_rate > 0.0


def test_mathieu_resonance_matches_reference_values() -> None:
    # La referencia usa Gamma=0.02; en nuestra convencion Gamma=2*zeta.
    parameters = LorentzParameters(
        damping_ratio=0.01,
        modulation_depth=0.20,
        modulation_ratio=2.0,
    )
    result = integrate_fundamental(parameters)
    expected = np.array([-1.133699226, -0.828351423], dtype=np.complex128)
    np.testing.assert_allclose(result.multipliers, expected, rtol=2e-7, atol=2e-8)
    assert np.isclose(result.max_growth_rate, 0.039943415, rtol=2e-6)


def test_modulation_phase_changes_matrix_but_not_floquet_spectrum() -> None:
    base = LorentzParameters(
        damping_ratio=0.025,
        modulation_depth=0.37,
        modulation_ratio=1.91,
        phase=0.0,
    )
    shifted = LorentzParameters(
        damping_ratio=base.damping_ratio,
        modulation_depth=base.modulation_depth,
        modulation_ratio=base.modulation_ratio,
        phase=1.137,
    )
    base_result = integrate_fundamental(base)
    shifted_result = integrate_fundamental(shifted)

    assert not np.allclose(base_result.matrix, shifted_result.matrix, rtol=1e-5)
    assert np.isclose(
        np.trace(base_result.matrix), np.trace(shifted_result.matrix), rtol=2e-10
    )
    assert np.isclose(
        base_result.determinant, shifted_result.determinant, rtol=2e-10
    )
