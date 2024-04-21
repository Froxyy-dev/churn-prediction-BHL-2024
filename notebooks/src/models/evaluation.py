from sklearn.metrics import roc_auc_score, f1_score, balanced_accuracy_score, confusion_matrix, ConfusionMatrixDisplay


def evaluate(clf, X, y):
    """Evaluate classifier on selected metrics"""
    metrics = {}

    y_pred = clf.predict(X)
    y_pred_proba = clf.predict_proba(X)[:, 1]

    metrics.update(roc_auc_score=roc_auc_score(y, y_pred_proba),
                   f1_score=f1_score(y, y_pred),
                   balanced_accuracy=balanced_accuracy_score(y, y_pred),
                   confusion_matrix=confusion_matrix(y, y_pred)
                   )
    return metrics


def print_confusion_matrix(clf, X, y):
    """Print prettified confusion matrix"""
    ConfusionMatrixDisplay.from_estimator(clf, X, y)
