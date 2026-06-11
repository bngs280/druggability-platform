from src.fpocket.parse_fpocket import parse
import pandas as pd


def build_features(info_file):

    pockets = parse(info_file)

    if len(pockets) == 0:
        return pd.DataFrame([{
            "PocketCount": 0,
            "MaxScore": 0,
            "MeanScore": 0,
            "MaxDruggability": 0,
            "MeanDruggability": 0,
            "MaxSASA": 0,
            "MeanSASA": 0
        }])

    scores = [p.get("Score", 0) for p in pockets]
    drug = [p.get("Druggability", 0) for p in pockets]
    sasa = [p.get("SASA", 0) for p in pockets]

    return pd.DataFrame([{
        "PocketCount": len(pockets),
        "MaxScore": max(scores),
        "MeanScore": sum(scores)/len(scores),
        "MaxDruggability": max(drug),
        "MeanDruggability": sum(drug)/len(drug),
        "MaxSASA": max(sasa),
        "MeanSASA": sum(sasa)/len(sasa)
    }])
