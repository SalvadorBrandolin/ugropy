import pytest

from ugropy import get_groups, psrk, unifac


# =============================================================================
# 51- NCO Main group: NCO
# =============================================================================

# UNIFAC
trials_unifac = [
    # Isophorone diisocyanate
    (
        "CC1(CC(CC(C1)(C)CN=C=O)N=C=O)C",
        {"CH3": 3, "CH2": 4, "CH": 1, "C": 2, "NCO": 2},
        "smiles",
    ),
]


@pytest.mark.UNIFAC
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_thiophene_unifac(identifier, result, identifier_type):
    assert get_groups(unifac, identifier, identifier_type).subgroups == result


@pytest.mark.PSRK
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_thiophene_psrk(identifier, result, identifier_type):
    assert get_groups(psrk, identifier, identifier_type).subgroups == {}
