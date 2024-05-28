from pathlib import Path

import numpy as np

import pandas as pd

from ugropy import abdulelah_gani_primary, get_groups


here = Path(__file__).parent.resolve()
df = pd.read_csv(f"{here}/dataset/Tm_results_GC.csv", index_col="SMILES")
df.columns = [int(col) if col.isdigit() else col for col in df.columns]

def get_primary_groups_from_df(smiles):
    row = df.loc[smiles, np.linspace(1, 220, 220, dtype=int)]
    row.replace(0.0, np.nan, inplace=True)
    
    if isinstance(row, pd.DataFrame):
        row = row.iloc[0]
    
    row.dropna(inplace=True)
    groups = row.to_dict()
    result = groups.copy()

    for group in groups.keys():
        group_name = abdulelah_gani_primary.subgroups[abdulelah_gani_primary.subgroups["group_number"] == group].index[0]

        result[group_name] = int(result.pop(group))

    return result


def test_tm_results():
    for smiles in df.index:
        exp = get_primary_groups_from_df(smiles)
        print(smiles)
        print(exp)
        model = get_groups(abdulelah_gani_primary, smiles, "smiles").subgroups

        assert exp == model