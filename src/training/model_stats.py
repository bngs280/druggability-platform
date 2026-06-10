import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


# =========================
# LOAD DATA + MODEL
# =========================
df = pd.read_csv("data/features/file1_with_compounds.csv")

df = df.dropna()
df["target"] = np.log1p(df["Compound"])

X = df.drop(columns=["Compound", "target", "UniProt"])
y = df["target"]

model = joblib.load("data/models/druggability_xgb.pkl")


# =========================
# SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# =========================
# PREDICT
# =========================
y_pred = model.predict(X_test)

# =========================
# METRICS
# =========================
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL STATISTICS =====")
print("RMSE:", rmse)
print("MAE :", mae)
print("R2  :", r2)