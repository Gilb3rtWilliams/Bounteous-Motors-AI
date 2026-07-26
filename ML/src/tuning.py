"""
tuning.py

Performs hyperparameter tuning.
"""

from sklearn.model_selection import RandomizedSearchCV

from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
)

from xgboost import XGBRegressor

from sklearn.pipeline import Pipeline

from config import (
    RANDOM_STATE,
    CV_FOLDS,
)

# ==========================================================
# Models
# ==========================================================

def get_models():

    return {

        "Linear Regression": LinearRegression(),

        "Decision Tree": DecisionTreeRegressor(
            random_state=RANDOM_STATE
        ),

        "Random Forest": RandomForestRegressor(
            random_state=RANDOM_STATE
        ),

        "Gradient Boosting": GradientBoostingRegressor(
            random_state=RANDOM_STATE
        ),

        "XGBoost": XGBRegressor(
            objective="reg:squarederror",
            random_state=RANDOM_STATE,
        ),
    }


# ==========================================================
# Parameter Grids
# ==========================================================

PARAMETERS = {

    "Random Forest": {

        "model__n_estimators": [200, 300, 400, 500],

        "model__max_depth": [10, 20, 30, None],

        "model__min_samples_split": [2, 5, 10],

        "model__min_samples_leaf": [1, 2, 4],

    },

    "Gradient Boosting": {

        "model__n_estimators": [100, 200, 300],

        "model__learning_rate": [0.01, 0.05, 0.1],

        "model__max_depth": [3, 5, 7],

    },

    "XGBoost": {

        "model__n_estimators": [200, 300, 500],

        "model__learning_rate": [0.01, 0.05, 0.1],

        "model__max_depth": [3, 5, 7],

        "model__subsample": [0.8, 1.0],

        "model__colsample_bytree": [0.8, 1.0],

    }

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

    if model_name not in PARAMETERS:

        print("No tuning required.")

        return model

    pipeline = Pipeline(

        steps=[

            ("preprocessor", preprocessor),

            ("model", model),

        ]

    )

    search = RandomizedSearchCV(

        estimator=pipeline,

        param_distributions=PARAMETERS[model_name],

        cv=CV_FOLDS,

        n_iter=15,

        scoring="r2",

        random_state=RANDOM_STATE,

        n_jobs=-1,

        verbose=1,

    )

    search.fit(

        X_train,

        y_train,

    )

    print(

        f"Best CV Score : "

        f"{search.best_score_:.4f}"

    )

    return search.best_estimator_.named_steps["model"]