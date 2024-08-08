import numpy as np
from sklearn.model_selection import train_test_split
from src.constants import CAT_FEATURES, TARGET_FEATURE, SEED


def build_features(data):
    """ Generates X matrix of features and y vector of targets"""
    data = data.drop(columns=["ServiceArea"])
    data.Churn = data.Churn.replace({"Yes": 1, "No": 0})

    data[CAT_FEATURES] = data[CAT_FEATURES].fillna("NaN")
    data[CAT_FEATURES] = data[CAT_FEATURES].astype("category")
    data = data.fillna(np.nan)

    y = data[TARGET_FEATURE]
    X = data.drop(columns=[TARGET_FEATURE, "CustomerID"])

    return X, y


def train_val_test_split(X, y):
    """ Split data into train, validation, and test sets"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.08, random_state=SEED)

    return X_train, X_val, X_test, y_train, y_val, y_test
