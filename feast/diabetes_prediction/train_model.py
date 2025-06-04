from feast import FeatureStore
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump

store = FeatureStore(repo_path="feature_repo")

entity_df = pd.read_parquet("feature_repo/data/target_df.parquet")

training_data = store.get_historical_features(
    entity_df=entity_df,
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
)

df = training_data.to_df()

# Model training
X = df.drop(columns=["Outcome", "event_timestamp", "patient_id"])
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

dump(model, "model/model.joblib")
print("✅ Model trained and saved.")
