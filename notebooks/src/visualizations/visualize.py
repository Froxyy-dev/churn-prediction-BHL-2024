import numpy as np
import shap
import matplotlib.pyplot as plt


def plot_shap_beeswarm(clf, X, y):
    """Plot Shapley Beeswarm plot"""
    explainer = shap.TreeExplainer(clf)
    shap_values = explainer(X)
    shap.plots.beeswarm(shap_values, max_display=20)


def plot_featue_importance(clf, X, y):
    """"Plot the individual importance values for each of the input features"""
    feature_importance = clf.feature_importances_
    sorted_idx = np.argsort(feature_importance)
    plt.figure(figsize=(12, 6))
    plt.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align="center")
    plt.yticks(range(len(sorted_idx)), np.array(X.columns)[sorted_idx])
    plt.title("Feature Importance")
