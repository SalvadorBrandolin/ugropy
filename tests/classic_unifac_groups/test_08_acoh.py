import pytest

from ugropy import constantinou_gani_primary, get_groups, psrk, unifac
from ugropy.core import fit_atoms


# =============================================================================
# 8- ACOH Main group: ACOH
# =============================================================================

# UNIFAC
trials_unifac = [
    # Phenanthrene-3,4-diol
    (
        "C1=CC=C2C(=C1)C=CC3=C2C(=C(C=C3)O)O",
        {"ACH": 8, "AC": 4, "ACOH": 2},
        "smiles",
    ),
    # 3-(tert-butyl)benzene-1,2-diol
    (
        "CC(C)(C)C1=C(C(=CC=C1)O)O",
        {"ACH": 3, "AC": 1, "ACOH": 2, "CH3": 3, "C": 1},
        "smiles",
    ),
    # [1,1'-Biphenyl]-2,3',4-triol
    (
        "C1=CC(=CC(=C1)O)C2=C(C=C(C=C2)O)O",
        {"ACH": 7, "AC": 2, "ACOH": 3},
        "smiles",
    ),
    ("C1=CC=C(C=C1)O", {"ACH": 5, "ACOH": 1}, "smiles"),
]


@pytest.mark.UNIFAC
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_acoh_unifac(identifier, result, identifier_type):
    mol = get_groups(unifac, identifier, identifier_type)
    assert mol.subgroups == result
    assert fit_atoms(mol.mol_object, mol.subgroups, unifac) != {}


@pytest.mark.PSRK
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_acoh_psrk(identifier, result, identifier_type):
    mol = get_groups(psrk, identifier, identifier_type)
    assert mol.subgroups == result
    assert fit_atoms(mol.mol_object, mol.subgroups, psrk) != {}


@pytest.mark.ConstantinouGani
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_acoh_cg(identifier, result, identifier_type):
    mol = get_groups(constantinou_gani_primary, identifier, identifier_type)
    assert mol.subgroups == result
    assert (
        fit_atoms(mol.mol_object, mol.subgroups, constantinou_gani_primary)
        != {}
    )
