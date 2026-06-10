import pandas as pd

from src.fpocket.parse_fpocket import parse


def build(info):

    pockets=parse(info)

    n=len(pockets)

    if n==0:

        return None

    scores=[]

    drug=[]

    sasa=[]

    for p in pockets:

        scores.append(
            p.get(
                "Score",
                0
            )
        )

        drug.append(
            p.get(
                "Druggability",
                0
            )
        )

        sasa.append(
            p.get(
                "SASA",
                0
            )
        )

    row={

        "PocketCount":n,

        "MaxScore":max(scores),

        "MeanScore":sum(scores)/n,

        "MaxDruggability":max(drug),

        "MeanDruggability":sum(drug)/n,

        "MaxSASA":max(sasa),

        "MeanSASA":sum(sasa)/n

    }

    return pd.DataFrame([row])


if __name__=="__main__":

    df=build(
        "data/pdb/P68871_out/P68871_info.txt"
    )

    print(df)