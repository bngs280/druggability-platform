import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
)

from xgboost import XGBClassifier

# 🔥 SMOTE IMPORT
from imblearn.over_sampling import SMOTE


INPUT = "data/features/features_with_label.csv"
MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)


# -----------------------
# Load data
# -----------------------

df = pd.read_csv(INPUT)

X = df.drop(columns=["UniProt", "label"])
y = df["label"]


# -----------------------
# Train/Test split
# -----------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42,
)


# -----------------------
# SMOTE (ONLY TRAIN DATA)
# -----------------------

smote = SMOTE(random_state=42)

X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

print("\nAfter SMOTE:")
print(y_train_res.value_counts())


# -----------------------
# Model (NO NEED scale_pos_weight now)
# -----------------------

model = XGBClassifier(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=42,
)


# -----------------------
# Train
# -----------------------

model.fit(X_train_res, y_train_res)


# -----------------------
# Prediction
# -----------------------

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]


# -----------------------
# Evaluation
# -----------------------

print("\nAccuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))
print("ROC AUC  :", roc_auc_score(y_test, y_prob))

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))


# -----------------------
# Save model
# -----------------------

joblib.dump(model, os.path.join(MODEL_DIR, "druggability.pkl"))
joblib.dump(list(X.columns), os.path.join(MODEL_DIR, "feature_columns.pkl"))

print("\nModel saved.")
print("Feature list saved.")

