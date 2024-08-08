import pandas as pd
import numpy as np
import category_encoders as ce


NUM_COLUMNS_MISSING = [
    'MonthlyRevenue',
    'MonthlyMinutes',
    'TotalRecurringCharge',
    'DirectorAssistedCalls',
    'OverageMinutes',
    'RoamingCalls',
    'PercChangeMinutes',
    'PercChangeRevenues',
    'AgeHH1',
    'AgeHH2',
]


def handle_missing_values(df, column_name):
    # Adding column indicating missing value.
    df[f"{column_name}_missing"] = df[column_name].isnull().astype(int)

    # Filling missing values with mean.
    mean_value = df[column_name].mean()

    if df[column_name].dtype == 'int64':
        mean_value = round(mean_value)

    df[column_name].fillna(mean_value, inplace=True)


def clean_dataframe(df):
    for column in NUM_COLUMNS_MISSING:
        handle_missing_values(df, column)

    encoder = ce.TargetEncoder(cols=['ServiceArea'])
    df['ServiceArea'] = encoder.fit_transform(df['ServiceArea'], df['Churn'].map({'Yes': 1, 'No': 0}))
