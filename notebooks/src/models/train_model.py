from catboost import CatBoostClassifier

from src.models.model_config import DEFAULT_PARAMS, BEST_PARAMS_FOUND


def train_model(X, y):
    """Train CatBoost classifier"""
    clf = CatBoostClassifier(**DEFAULT_PARAMS, **BEST_PARAMS_FOUND)
    clf.fit(X, y)

    return clf
