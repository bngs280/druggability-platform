import pandas as pd

from xgboost import XGBClassifier

import joblib

df = pd.read_csv(
    "data/features/training_data.csv"
)

X = df.drop(
    columns=["label"]
)

y = df["label"]

model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    random_state=42
)

model.fit(
    X,
    y
)

joblib.dump(
    model,
    "data/models/druggability.pkl"
)

print("Model saved")