import json

from rdkit import Chem
from rdkit.Chem import Descriptors

import numpy as np

import pandas as pd


def get_groups(chem_object, subgroups, subgroups_matrix, problematic_structures):
    # Shorter names for dataframes:
    df = subgroups
    dfm = subgroups_matrix
    df_problematics = problematic_structures

    # Groups and occurence number in chem_object:
    groups = np.array([])
    many_groups = np.array([])

    # =========================================================================
    # Detect present functional groups in the molecule
    # =========================================================================
    for group in df.index:
        smarts = df.loc[group]["smarts"]

        func_group = Chem.MolFromSmarts(smarts)
        matches = chem_object.GetSubstructMatches(func_group)
        how_many_matches = len(matches)
        
        if how_many_matches > 0:
            groups = np.append(groups, group)
            many_groups = np.append(many_groups, how_many_matches).astype(int)

    dff = dfm.loc[groups][groups]
    dff = dff.mul(many_groups, axis= 0)

    for smarts in df_problematics.index:
        structure = Chem.MolFromSmarts(smarts)
        matches = chem_object.GetSubstructMatches(structure)
        how_many_problems = len(matches)

        if how_many_problems > 0:
            problm_dict = json.loads(df_problematics.loc[smarts].contribute)

            for grp in problm_dict.keys():
                dff.loc[grp][grp] += problm_dict[grp] * how_many_problems


    dff_sum = dff.sum(axis=0)
    dff_sum.replace(0, pd.NA, inplace=True)
    dff_final = dff_sum.dropna()

    return dff_final.to_dict()