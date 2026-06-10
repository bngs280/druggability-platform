import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split


df = pd.read_csv("data/features/file1_with_compounds.csv")

df = df.dropna()
df["target"] = np.log1p(df["Compound"])

X = df.drop(columns=["Compound", "target", "UniProt"])
y = df["target"]

model = joblib.load("data/models/druggability_xgb.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

y_pred = model.predict(X_test)

# convert back to real compounds
y_test_real = np.expm1(y_test)
y_pred_real = np.expm1(y_pred)

# accuracy as "within tolerance"
tolerance = 0.2  # 20%

correct = np.abs(y_test_real - y_pred_real) / (y_test_real + 1e-9) < tolerance

accuracy = np.mean(correct)

print("\n===== ACCURACY (BIO-REALISTIC) =====")
print("Accuracy within 20% error:", accuracy)