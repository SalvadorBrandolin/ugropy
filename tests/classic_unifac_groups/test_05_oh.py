import pytest

from ugropy import constantinou_gani_primary, get_groups, psrk, unifac
from ugropy.core import fit_atoms


# =============================================================================
# 5- OH Main group: OH
# =============================================================================

# UNIFAC
trials_unifac = [
    # 1,2-Cyclohexanediol, 4-tert-butyl-1-phenyl-, stereoisomer
    (
        "CC(C)(C)C1CCC(C(C1)O)(C2=CC=CC=C2)O",
        {"CH3": 3, "CH2": 3, "CH": 2, "C": 2, "OH": 2, "AC": 1, "ACH": 5},
        "smiles",
    ),
    # (2S,3S)-2-Methyl-1,3-hexanediol
    ("CCCC(C(C)CO)O", {"CH3": 2, "CH2": 3, "CH": 2, "OH": 2}, "smiles"),
    # 2-propanol
    ("CC(C)O", {"CH3": 2, "CH": 1, "OH": 1}, "smiles"),
    ("OC(O)=O", {"COOH": 1, "OH": 1}, "smiles"),
]


@pytest.mark.UNIFAC
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_oh_unifac(identifier, result, identifier_type):
    mol = get_groups(unifac, identifier, identifier_type)
    assert mol.subgroups == result
    assert fit_atoms(mol.mol_object, mol.subgroups, unifac) != {}


@pytest.mark.PSRK
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_oh_psrk(identifier, result, identifier_type):
    mol = get_groups(psrk, identifier, identifier_type)
    assert mol.subgroups == result
    assert fit_atoms(mol.mol_object, mol.subgroups, psrk) != {}


@pytest.mark.ConstantinouGani
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_oh_cg(identifier, result, identifier_type):
    mol = get_groups(constantinou_gani_primary, identifier, identifier_type)
    assert mol.subgroups == result
    assert (
        fit_atoms(mol.mol_object, mol.subgroups, constantinou_gani_primary)
        != {}
    )
