from src.inference.download_structure import download_pdb
from src.inference.run_fpocket import run_fpocket
from src.inference.features import build_features
from src.inference.model import predict


def predict_from_uniprot(uniprot_id):

    print(f"\n[1] Downloading structure for {uniprot_id}")
    pdb_file = download_pdb(uniprot_id)

    print("[2] Running fpocket")
    info_file = run_fpocket(pdb_file)

    print("[3] Building features")
    features = build_features(info_file)

    print("[4] Running ML model")
    pred, prob = predict(features)

    return {
        "uniprot": uniprot_id,
        "prediction_class": int(pred),
        "probability": {
            "class0": float(prob[0]),
            "class1": float(prob[1])
        },
        "score": float(prob[1])
    }
