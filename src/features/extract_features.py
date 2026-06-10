import os
import pandas as pd
from src.fpocket.parse_fpocket import parse


def build(info_file):

    pockets = parse(info_file)

    n = len(pockets)

    if n == 0:
        return None

    scores, drug, sasa = [], [], []

    for p in pockets:
        scores.append(p.get("Score", 0))
        drug.append(p.get("Druggability", 0))
        sasa.append(p.get("SASA", 0))

    protein = os.path.basename(info_file).replace("_info.txt", "")

    row = {
        "UniProt": protein,
        "PocketCount": n,
        "MaxScore": max(scores),
        "MeanScore": sum(scores) / n,
        "MaxDruggability": max(drug),
        "MeanDruggability": sum(drug) / n,
        "MaxSASA": max(sasa),
        "MeanSASA": sum(sasa) / n
    }

    return pd.DataFrame([row])


def build_all(base_dir):
    all_dfs = []

    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith("_info.txt"):
                path = os.path.join(root, f)

                df = build(path)
                if df is not None:
                    all_dfs.append(df)

    if len(all_dfs) == 0:
        return pd.DataFrame()

    return pd.concat(all_dfs, ignore_index=True)


if __name__ == "__main__":

    base_dir = "data/pdb"

    df = build_all(base_dir)

    print(df)

    # optional save
    df.to_csv("data/features/features.csv", index=False)

# import pandas as pd

# from src.fpocket.parse_fpocket import parse


# def build(info):

#     pockets=parse(info)

#     n=len(pockets)

#     if n==0:

#         return None

#     scores=[]

#     drug=[]

#     sasa=[]

#     for p in pockets:

#         scores.append(
#             p.get(
#                 "Score",
#                 0
#             )
#         )

#         drug.append(
#             p.get(
#                 "Druggability",
#                 0
#             )
#         )

#         sasa.append(
#             p.get(
#                 "SASA",
#                 0
#             )
#         )

#     row={

#         "PocketCount":n,

#         "MaxScore":max(scores),

#         "MeanScore":sum(scores)/n,

#         "MaxDruggability":max(drug),

#         "MeanDruggability":sum(drug)/n,

#         "MaxSASA":max(sasa),

#         "MeanSASA":sum(sasa)/n

#     }

#     return pd.DataFrame([row])


# if __name__=="__main__":

#     df=build(
#         "data/pdb/P68871_out/P68871_info.txt"
#     )

#     print(df)