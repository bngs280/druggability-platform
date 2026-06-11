import pandas as pd
import joblib

# Load model
model = joblib.load("models/druggability.pkl")

# IMPORTANT: must match training feature names EXACTLY
sample = pd.DataFrame([{

    "PocketCount": 5,
    "MaxScore": 0.8,
    "MeanScore": 0.5,
    "MaxDruggability": 0.75,
    "MeanDruggability": 0.6,
    "MaxSASA": 800,
    "MeanSASA": 300

}])

# Predict class
pred = model.predict(sample)[0]

# Predict probability
prob = model.predict_proba(sample)[0]

print("Prediction (class):", pred)
# print("Probability [class0, class1]:", prob)
print(f"Class 0 (non-druggable): {prob[0]*100:.2f}%")
print(f"Class 1 (druggable)    : {prob[1]*100:.2f}%")