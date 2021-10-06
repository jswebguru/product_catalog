import pandas as pd
import os
import re

EQUIPMENT_COLS = {
    "excavators": [],
    "wheel-loaders": [],
    "backhoe": [],
    "skidsteer": [],
    "dump-trucks": [],
    "dozers": [],
    "motor-graders": [],
    "crushers": [],
}

df = pd.read_csv("../data/equipment_specifications_raw.csv")


def sort_by_colnames(df):
    return df.sort_index(axis=1, ascending=True)


def split_equipment_types(df):
    for col in df.columns:
        for equipment_type in EQUIPMENT_COLS.keys():
            if re.match(f"{equipment_type}", col):
                EQUIPMENT_COLS[equipment_type].append(col)

    for equipment_type, equipment_cols in EQUIPMENT_COLS.items():
        equipment_df = df.loc[:, equipment_cols]
        equipment_df.dropna(axis=0, how="all", inplace=True)
        equipment_df.to_csv(f"../data/{equipment_type}.csv", index=False)
        

if __name__ == "__main__":
    sorted_df = sort_by_colnames(df=df)
    split_equipment_types(sorted_df)