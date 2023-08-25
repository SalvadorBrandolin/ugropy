from rdkit import Chem

import pubchempy as pcp

from .core.get_groups import get_groups

from .constants import unifac_subgroups, unifac_matrix, problematic_structures

class Groups:
    def __init__(self, identifier, identifier_type="name") -> None:
        
        self.identifier = identifier.lower()
        self.identifier_type = identifier_type.lower()

        if self.identifier_type == "smiles":
            self.smiles = identifier
            chem_object = Chem.MolFromSmiles(self.smiles)
        else:
            pcp_object = pcp.get_compounds(self.identifier, self.identifier_type)[0]
            self.smiles = pcp_object.canonical_smiles
            chem_object = Chem.MolFromSmiles(self.smiles)

        self.unifac_groups = get_groups(
            chem_object, 
            unifac_subgroups, 
            unifac_matrix,
            problematic_structures
        )
        