import pandas as pd
import numpy as np

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib


# =========================
# 1. LOAD DATA
# =========================
# Expected columns:
# MaxScore, MeanDruggability, MaxSASA, MeanSASA, PocketCount, Compound

df = pd.read_csv("data/features/file1_with_compounds.csv")

print("Dataset shape:", df.shape)
def assign_class(x):
    if x <= 10:
        return 0   # low
    elif x <= 100:
        return 1   # medium
    else:
        return 2   # high


df["target_class"] = df["Compound"].apply(assign_class)

print(df["target_class"].value_counts())
# =========================
# 2. BASIC CLEANING
# =========================
df = df.dropna()

# Remove invalid compound values
df = df[df["Compound"] >= 0]

# =========================
# 3. TARGET TRANSFORMATION
# =========================
# Why log?
# Compound are highly skewed (1 to 5000+)
df["target"] = np.log1p(df["Compound"])

# =========================
# 4. FEATURES / LABEL SPLIT
# =========================
X = df.drop(columns=["Compound", "target", "UniProt",  "target_class"])
y = df["target_class"]

print("Features:", list(X.columns))

# =========================
# 5. TRAIN / TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 6. MODEL (XGBOOST REGRESSOR)
# =========================
model = XGBRegressor(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="mlogloss"
)

# =========================
# 7. TRAINING
# =========================
model.fit(X_train, y_train)

# =========================
# 8. PREDICTION
# =========================
y_pred = model.predict(X_test)

# =========================
# 9. EVALUATION
# =========================
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL PERFORMANCE =====")
print("RMSE:", rmse)
print("R2 Score:", r2)

# =========================
# 10. CONVERT BACK TO Compound
# =========================
y_test_real = np.expm1(y_test)
y_pred_real = np.expm1(y_pred)

print("\nSample predictions:")
for i in range(5):
    print(f"Actual: {y_test_real.iloc[i]:.2f} | Predicted: {y_pred_real[i]:.2f}")

# =========================
# 11. SAVE MODEL
# =========================
joblib.dump(model, "data/models/druggability_xgb.pkl")

print("\nModel saved → data/models/druggability_xgb.pkl")

# import pandas as pd

# from xgboost import XGBClassifier

# import joblib

# df = pd.read_csv(
#     "data/features/features.csv"
# )

# X = df.drop(
#     columns=["label"]
# )

# y = df["label"]

# model = XGBClassifier(
#     n_estimators=200,
#     max_depth=5,
#     learning_rate=0.05,
#     random_state=42
# )

# model.fit(
#     X,
#     y
# )

# joblib.dump(
#     model,
#     "data/models/druggability.pkl"
# )

# print("Model saved")