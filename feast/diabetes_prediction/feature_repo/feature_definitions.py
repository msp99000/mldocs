from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64, Int64

# 1. Define entity
patient = Entity(name="patient", join_keys=["patient_id"])

# 2. Define data sources
predictors_source = FileSource(
    path="data/predictors_df.parquet",
    event_timestamp_column="event_timestamp",
)

target_source = FileSource(
    path="data/target_df.parquet",
    event_timestamp_column="event_timestamp",
)

# 3. Define Feature Views
predictors_fv = FeatureView(
    name="predictors_df_feature_view",
    ttl=timedelta(days=2),
    entities=[patient],
    schema=[
        Field(name="Pregnancies", dtype=Int64),
        Field(name="Glucose", dtype=Int64),
        Field(name="BloodPressure", dtype=Int64),
        Field(name="SkinThickness", dtype=Int64),
        Field(name="Insulin", dtype=Int64),
        Field(name="BMI", dtype=Float64),
        Field(name="DiabetesPedigreeFunction", dtype=Float64),
        Field(name="Age", dtype=Int64),
    ],
    source=predictors_source,
    online=True,
)

target_fv = FeatureView(
    name="target_df_feature_view",
    ttl=timedelta(days=2),
    entities=[patient],
    schema=[
        Field(name="Outcome", dtype=Int64),
    ],
    source=target_source,
    online=True,
)
