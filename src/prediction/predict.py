import pandas as pd
import joblib

model = joblib.load(
    "data/models/druggability.pkl"
)

sample = pd.DataFrame([{

    "pocket_count":5,
    "max_volume":800,
    "mean_volume":300,
    "druggability_score":0.75

}])

pred = model.predict(sample)[0]

prob = model.predict_proba(sample)[0]

print("Prediction:", pred)

print("Probability:", prob)