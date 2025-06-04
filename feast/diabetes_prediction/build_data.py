import pandas as pd
import os

# Load dataset
data_url = "https://raw.githubusercontent.com/msp99000/mldocs/refs/heads/main/feast/diabetes_prediction/data/diabetes.csv"
data = pd.read_csv(data_url)

# Separate predictors and target
predictors_df = data.drop(columns=["Outcome"]).copy()  # Use .copy() to avoid warnings
target_df = data[["Outcome"]].copy()  # Use .copy() to avoid warnings

# Add event_timestamp
timestamps = pd.date_range(end=pd.Timestamp.now(), periods=len(data), freq='D')
predictors_df["event_timestamp"] = timestamps
target_df["event_timestamp"] = timestamps

# Create patient_id
predictors_df["patient_id"] = list(range(len(data)))
target_df["patient_id"] = list(range(len(data)))

# Make sure the feature_repo/data directory exists
os.makedirs("feature_repo/data", exist_ok=True)

# Save to Parquet format
predictors_df.to_parquet("feature_repo/data/predictors_df.parquet", index=False)
target_df.to_parquet("feature_repo/data/target_df.parquet", index=False)

print(f"Saved feature data to feature_repo/data/")
