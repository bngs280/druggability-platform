import joblib
import numpy as np

MODEL_PATH = "models/druggability.pkl"
model = joblib.load(MODEL_PATH)

FEATURES = joblib.load("models/feature_columns.pkl")


def predict(features_df):

    # align columns
    features_df = features_df[FEATURES]

    pred = model.predict(features_df)[0]
    prob = model.predict_proba(features_df)[0]

    return pred, prob
