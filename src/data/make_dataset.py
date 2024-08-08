import pandas as pd


def load_local_dataset():
    """Read local dataset"""
    data = pd.read_csv("../data/telecom/cell2celltrain.csv")
    return data
