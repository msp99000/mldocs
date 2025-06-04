from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="feature_repo")

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

print(features)
