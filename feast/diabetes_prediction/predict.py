import pandas as pd
from joblib import load

# Load the trained model
model = load("model/model.joblib")

# Load online features
features = pd.read_csv("online_features.csv")  # or from get_online_features.py
X = features.drop(columns=["patient_id"])

preds = model.predict(X)
probs = model.predict_proba(X)

print("Predictions:", preds)
print("Probabilities:", probs)
