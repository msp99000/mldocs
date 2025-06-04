# FEAST: Feature Store for Machine Learning

Feast (Feature Store) is an operational data system for managing and serving machine learning features to models in production. This repository demonstrates how to use Feast for feature management in a diabetes prediction use case.

## What is Feast?

Feast helps you:

- Define features once and use them across training and inference
- Generate training datasets with point-in-time correct feature values
- Serve features to models with low latency
- Avoid training-serving skew by using consistent feature transformations

## Repository Structure

```
feast/
├── diabetes_prediction
│   ├── __init__.py
│   ├── build_data.py
│   ├── data
│   │   └── diabetes.csv
│   ├── feature_repo
│   │   ├── __init__.py
│   │   ├── data
│   │   │   ├── online_store.db
│   │   │   ├── predictors_df.parquet
│   │   │   ├── registry.db
│   │   │   └── target_df.parquet
│   │   ├── feature_definitions.py
│   │   └── feature_store.yaml
│   ├── get_online_features.py
│   ├── model
│   │   └── model.joblib
│   ├── predict.py
│   ├── README.md
│   ├── run_pipeline.py
│   └── train_model.py
└── README.md
```

## Getting Started with Diabetes Prediction Example

### Prerequisites

- Python 3.8+
- Feast (`pip install feast`)
- Scikit-learn (`pip install scikit-learn`)
- Pandas (`pip install pandas`)

### Running the Example

The diabetes prediction example demonstrates a complete ML workflow using Feast:

1. Clone this repository
2. Navigate to the project directory: `cd feast/diabetes_prediction`
3. Run the end-to-end pipeline: `python run_pipeline.py`

The pipeline will:

1. Build feature data from the diabetes dataset
2. Register feature definitions with Feast
3. Train a logistic regression model
4. Materialize features to the online store
5. Retrieve online features and make predictions

### Key Components

- **Feature Repository**: Defines feature views, entities, and data sources
- **Offline Store**: Stores historical feature values for training
- **Online Store**: Stores latest feature values for predictions
- **Feature Registry**: Tracks feature metadata and definitions

## Extending This Project

To adapt this project for your own use case:

1. Create feature definitions in `feature_definitions.py`
2. Define your data sources and schemas
3. Configure your `feature_store.yaml` for your environment
4. Build training pipelines using `get_historical_features()`
5. Build serving pipelines using `get_online_features()`

## Best Practices

- Use consistent feature definitions across training and serving
- Keep the feature registry in version control
- Schedule regular materialization for online features
- Monitor feature statistics for drift

## Learn More

- [Feast Documentation](https://docs.feast.dev/)
- [Feast GitHub Repository](https://github.com/feast-dev/feast)
