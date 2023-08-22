import ugropy as ug

import pytest


# =============================================================================
# 5- OH Main group: OH
# =============================================================================

# UNIFAC
trials_unifac = [
    # 1,2-Cyclohexanediol, 4-tert-butyl-1-phenyl-, stereoisomer
    ("CC(C)(C)C1CCC(C(C1)O)(C2=CC=CC=C2)O", {"CH3": 3, "CH2": 3, "CH": 2, "C": 2, "OH": 2, "AC": 1, "ACH": 5}, "smiles"),
    # (2S,3S)-2-Methyl-1,3-hexanediol
    ("CCCC(C(C)CO)O", {"CH3": 2, "CH2": 3, "CH": 2, "OH": 2}, "smiles"),
    ("2-propanol", {"CH3": 2, "CH": 1, "OH": 1}, "name"),
]

@pytest.mark.OH
@pytest.mark.UNIFAC
@pytest.mark.parametrize("identifier, result, identifier_type", trials_unifac)
def test_oh_unifac(identifier, result, identifier_type):
    groups = ug.Groups(identifier, identifier_type)
    assert groups.unifac_groups == result