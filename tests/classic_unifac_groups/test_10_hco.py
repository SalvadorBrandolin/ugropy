import pytest

from ugropy import constantinou_gani_primary, get_groups, psrk, unifac
from ugropy.core import fit_atoms


# =============================================================================
# 10- HCO Main group (aldehyde): HCO
# =============================================================================

# UNIFAC
trials_unifac = [
    ("C(=O)C=O", {"HCO": 2}, "smiles"),
    # salicylaldehyde
    (
        "C1=CC=C(C(=C1)C=O)O",
        {"ACH": 4, "ACOH": 1, "AC": 1, "HCO": 1},
        "smiles",
    ),
    # 2-Methyl-3-butenal
    ("CC(C=C)C=O", {"CH3": 1, "CH": 1, "CH2=CH": 1, "HCO": 1}, "smiles"),
    # Cinnamaldehyde
    (
        "C1=CC=C(C=C1)C=CC=O",
        {"ACH": 5, "AC": 1, "CH=CH": 1, "HCO": 1},
        "smiles",
    ),
    # benzaldehyde
    ("C1=CC=C(C=C1)C=O", {"ACH": 5, "AC": 1, "HCO": 1}, "smiles"),
    # cyclohexanecarbaldehyde
    (
        "C1CCC(CC1)C=O",
        {
            "CH2": 5,
            "CH": 1,
            "HCO": 1,
        },
        "smiles",
    ),
    # pentanal
    ("CCCCC=O", {"CH3": 1, "CH2": 3, "HCO": 1}, "smiles"),
    # 3-methylbutanal
    ("CC(C)CC=O", {"CH3": 2, "CH2": 1, "CH": 1, "HCO": 1}, "smiles"),
    # acetaldehyde
    ("CC=O", {"CH3": 1, "HCO": 1}, "smiles"),
    # 2-Hexyl-3-Phenyl-2-Propenal
    (
        r"CCCCCC\C(C=O)=C/C1=CC=CC=C1",
        {"ACH": 5, "AC": 1, "CH=C": 1, "CH2": 5, "CH3": 1, "HCO": 1},
        "smiles",
    ),
]


@pytest.mark.UNIFAC
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_hco_unifac(identifier, result, identifier_type):
    mol = get_groups(unifac, identifier, identifier_type)
    assert mol.subgroups == result
    assert fit_atoms(mol.mol_object, mol.subgroups, unifac) != {}


@pytest.mark.PSRK
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_hco_psrk(identifier, result, identifier_type):
    mol = get_groups(psrk, identifier, identifier_type)
    assert mol.subgroups == result
    assert fit_atoms(mol.mol_object, mol.subgroups, psrk) != {}


@pytest.mark.ConstantinouGani
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_hco_cg(identifier, result, identifier_type):
    mol = get_groups(constantinou_gani_primary, identifier, identifier_type)
    assert mol.subgroups == result
    assert (
        fit_atoms(mol.mol_object, mol.subgroups, constantinou_gani_primary)
        != {}
    )
