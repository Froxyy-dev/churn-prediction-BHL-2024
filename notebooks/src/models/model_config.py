from src.constants import CAT_FEATURES, SEED


DEFAULT_PARAMS = {
    "objective": "Logloss",
    "iterations": 1000,
    "eval_metric": "Accuracy",
    "logging_level": "Silent",
    "cat_features": CAT_FEATURES,
    "random_state": SEED,
}

BEST_PARAMS_FOUND = {
    "colsample_bylevel": 0.07096471660444076,
    "depth": 2,
    "boosting_type": "Plain",
    "bootstrap_type": "MVS",
    "auto_class_weights": "SqrtBalanced",
    "learning_rate": 0.07805723502510105,
    "l2_leaf_reg": 3.359610782626036,
    "border_count": 228
}
