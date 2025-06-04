# Diabetes Prediction with Feast

This project demonstrates how to use Feast (Feature Store) to build a diabetes prediction model. It shows the complete workflow from feature definition to model serving.

## Project Overview

The diabetes prediction model uses health metrics like glucose levels, BMI, and blood pressure to predict diabetes risk. Feast manages feature values, ensuring consistency between training and inference.

## Directory Structure

```
├── __init__.py
├── build_data.py
├── data
│   └── diabetes.csv
├── feature_repo
│   ├── __init__.py
│   ├── data
│   │   ├── online_store.db
│   │   ├── predictors_df.parquet
│   │   ├── registry.db
│   │   └── target_df.parquet
│   ├── feature_definitions.py
│   └── feature_store.yaml
├── get_online_features.py
├── model
│   └── model.joblib
├── predict.py
├── README.md
├── run_pipeline.py
└── train_model.py
```

## How to Run

### One-Step Execution

The simplest way to run the entire pipeline is:

```bash
python run_pipeline.py
```

This script will:

1. Build feature data from the diabetes dataset
2. Apply Feast feature definitions
3. Train a logistic regression model
4. Materialize features to the online store
5. Retrieve online features and make predictions

### Step-by-Step Execution

If you prefer to run each step individually:

1. **Prepare data**

   ```bash
   python build_data.py
   ```

2. **Apply feature definitions**

   ```bash
   cd feature_repo
   feast apply
   cd ..
   ```

3. **Train the model**

   ```bash
   python train_model.py
   ```

4. **Materialize features**

   ```bash
   cd feature_repo
   feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")
   cd ..
   ```

5. **Retrieve features and predict**
   ```bash
   python get_online_features.py
   python predict.py
   ```

## Key Files Explained

- **feature_definitions.py**: Defines the patient entity and feature views for predictors and target
- **build_data.py**: Prepares the diabetes dataset and adds required timestamps and entity IDs
- **train_model.py**: Retrieves historical features and trains a logistic regression model
- **get_online_features.py**: Demonstrates how to retrieve the latest feature values
- **predict.py**: Applies the trained model to make diabetes predictions

## Production Considerations

For production deployment, consider:

1. Using a more scalable offline store like BigQuery, Snowflake, or Redshift
2. Setting up a remote registry for feature definitions
3. Implementing scheduled materialization with Airflow
4. Deploying a feature server with `feast serve`
5. Setting up monitoring for feature drift

## Learn More

- [Feast Documentation](https://docs.feast.dev/)
- [Running Feast in Production](https://docs.feast.dev/how-to-guides/running-feast-in-production)
- [Feature Retrieval](https://docs.feast.dev/getting-started/concepts/feature-retrieval)
