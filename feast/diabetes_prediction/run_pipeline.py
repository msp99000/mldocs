"""
Complete Diabetes Prediction Pipeline
This script orchestrates the entire workflow:
1. Builds the feature data
2. Applies the Feast feature definitions
3. Trains the model
4. Materializes features to the online store
5. Gets online features and makes predictions
"""

import os
import subprocess
import pandas as pd
from feast import FeatureStore
from joblib import load
import sys

def run_step(step_name, function):
    print(f"\n{'=' * 40}")
    print(f"STEP: {step_name}")
    print(f"{'=' * 40}")
    function()
    print(f"✅ Completed: {step_name}")

def build_data():
    print("Building feature data...")
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import build_data
    print("Data built and saved to feature_repo/data/")

def apply_feast():
    print("Applying Feast feature definitions...")
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "feature_repo"))
    from feature_definitions import patient, predictors_fv, target_fv
    
    store = FeatureStore(repo_path="feature_repo")
    # Pass the feature objects to the apply method
    store.apply([patient, predictors_fv, target_fv])
    print("Feature definitions applied")

def materialize_features():
    print("Materializing features to online store...")
    store = FeatureStore(repo_path="feature_repo")
    store.materialize_incremental(end_date=pd.Timestamp.now())
    print("Features materialized to online store")

def train_model():
    print("Training model...")
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import train_model
    print("Model trained and saved")

def get_online_features_and_predict():
    print("Getting online features and making predictions...")
    store = FeatureStore(repo_path="feature_repo")
    
    # Get online features
    features = store.get_online_features(
        features=[
            "predictors_df_feature_view:Pregnancies",
            "predictors_df_feature_view:Glucose",
            "predictors_df_feature_view:BloodPressure",
            "predictors_df_feature_view:SkinThickness",
            "predictors_df_feature_view:Insulin",
            "predictors_df_feature_view:BMI",
            "predictors_df_feature_view:DiabetesPedigreeFunction",
            "predictors_df_feature_view:Age",
        ],
        entity_rows=[
            {"patient_id": 767},
            {"patient_id": 766},
        ]
    ).to_df()
    
    print("\nOnline features retrieved:")
    print(features)
    
    # Load model and make predictions
    try:
        model = load("model/model.joblib")
        
        # Ensure features are in the correct order
        feature_columns = [
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
        ]
        
        # Reorder columns to match training data
        X = features[feature_columns]
        
        # Make predictions
        preds = model.predict(X)
        probs = model.predict_proba(X)
        
        print("\nPredictions:", preds)
        print("Probabilities:", probs)
    except FileNotFoundError:
        print("Model file not found. Run the training step first.")

if __name__ == "__main__":
    # Ensure we're in the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Create model directory if it doesn't exist
    os.makedirs("model", exist_ok=True)
    
    # Run the pipeline
    run_step("Building Data", build_data)
    run_step("Applying Feast Definitions", apply_feast)
    run_step("Training Model", train_model)
    run_step("Materializing Features", materialize_features)
    run_step("Getting Features and Predicting", get_online_features_and_predict)
    
    print("\n🎉 Pipeline completed successfully!")