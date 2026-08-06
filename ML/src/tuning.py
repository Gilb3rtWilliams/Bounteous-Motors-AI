"""
tuning.py

Performs hyperparameter tuning for candidate regression models.
"""

from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
)
from xgboost import XGBRegressor

from ML.src.config import (
    RANDOM_STATE,
    CV_FOLDS,
)


# ==========================================================
# Candidate Models
# ==========================================================

def get_models():
    """
    Return the candidate regression models.
    """

    return {

        "Linear Regression":
            LinearRegression(),

        "Decision Tree":
            DecisionTreeRegressor(
                random_state=RANDOM_STATE
            ),

        "Random Forest":
            RandomForestRegressor(
                random_state=RANDOM_STATE
            ),

        "Gradient Boosting":
            GradientBoostingRegressor(
                random_state=RANDOM_STATE
            ),

        "XGBoost":
            XGBRegressor(
                objective="reg:squarederror",
                random_state=RANDOM_STATE,
            ),
    }


# ==========================================================
# Hyperparameter Grids
# ==========================================================

PARAMETERS = {

    "Decision Tree": {

        "model__max_depth":
            [5, 10, 15, 20, None],

        "model__min_samples_split":
            [2, 5, 10],

        "model__min_samples_leaf":
            [1, 2, 4],
    },

    "Random Forest": {

        "model__n_estimators":
            [200, 300, 500],

        "model__max_depth":
            [10, 20, 30, None],

        "model__min_samples_split":
            [2, 5, 10],

        "model__min_samples_leaf":
            [1, 2, 4],
    },

    "Gradient Boosting": {

        "model__n_estimators":
            [100, 200, 300],

        "model__learning_rate":
            [0.01, 0.05, 0.1],

        "model__max_depth":
            [3, 5, 7],
    },

    "XGBoost": {

        "model__n_estimators":
            [200, 300, 500],

        "model__learning_rate":
            [0.01, 0.05, 0.1],

        "model__max_depth":
            [3, 5, 7],

        "model__subsample":
            [0.8, 1.0],

        "model__colsample_bytree":
            [0.8, 1.0],
    },
}


# ==========================================================
# Hyperparameter Tuning
# ==========================================================

def tune_model(
    model_name,
    model,
    X_train,
    y_train,
    preprocessor,
):
    """
    Tune a model using RandomizedSearchCV.

    Returns
    -------
    sklearn.pipeline.Pipeline
        Best fitted pipeline.
    """

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    if model_name not in PARAMETERS:

        print("✓ No tuning required.")

        pipeline.fit(X_train, y_train)

        return pipeline

    print(f"Running Random Search for {model_name}...")

    search = RandomizedSearchCV(
        estimator=pipeline,
        param_distributions=PARAMETERS[model_name],
        n_iter=15,
        scoring="r2",
        cv=CV_FOLDS,
        random_state=RANDOM_STATE,
        n_jobs=-1,
        verbose=1,
    )

    search.fit(X_train, y_train)

    print(f"✓ Best CV Score : {search.best_score_:.4f}")

    print(f"✓ Best Parameters:")

    for k, v in search.best_params_.items():
        print(f"   {k}: {v}")

    return search.best_estimator_