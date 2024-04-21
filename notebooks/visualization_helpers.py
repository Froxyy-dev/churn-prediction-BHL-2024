import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_bar_charts(df, columns):
    for column in columns:
        plt.figure(figsize=(16, 6))

        # Pierwszy wykres - wykres słupkowy dla kolumny
        plt.subplot(1, 2, 1)
        df[column].value_counts().plot(kind='bar')
        plt.title(f'Bar Chart for {column}')
        plt.xlabel(column)
        plt.ylabel('Count')

        # Drugi wykres - wykres słupkowy z kolorami zależnymi od kolumny 'churn'
        plt.subplot(1, 2, 2)
        sns.countplot(data=df, x=column, hue='Churn')
        plt.title(f'Bar Chart for {column} with Churn')
        plt.xlabel(column)
        plt.ylabel('Count')

        plt.tight_layout()
        plt.show()


def plot_histograms(df, columns):
    for column in columns:
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # Pierwszy wykres - histogram
        df[column].plot(kind='hist', bins=20, edgecolor='black', ax=axes[0])
        axes[0].set_title(f'Histogram for {column}')
        axes[0].set_xlabel(column)
        axes[0].set_ylabel('Frequency')

        # Drugi wykres - histogram z podziałem na churn
        sns.histplot(df, x=column, hue='Churn', multiple="stack", bins=20, edgecolor='black', ax=axes[1])
        axes[1].set_title(f'{column} by Churn histogram')
        axes[1].set_xlabel(column)
        axes[1].set_ylabel('Count')
        axes[1].legend(title='Churn', labels=['Not Churn', 'Churn'])

        plt.tight_layout()
        plt.show()


def plot_log_histograms(df, columns):
    for column in columns:
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # Pierwszy wykres - log histogram
        values = df[column].dropna()
        min_value = values.min()
        log_values = np.log(values - min_value + 1)
        axes[0].hist(log_values, bins=20, edgecolor='black')
        axes[0].set_title(f'Log Histogram for {column}')
        axes[0].set_xlabel(column)
        axes[0].set_ylabel('Frequency')

        # Drugi wykres - histogram z podziałem na churn
        cpy_df = df.copy()
        cpy_df[column] = log_values
        sns.histplot(cpy_df, x=column, hue='Churn', multiple="stack", bins=20, edgecolor='black', ax=axes[1])
        axes[1].set_title(f'{column} by Churn histogram')
        axes[1].set_xlabel(column)
        axes[1].set_ylabel('Count')
        axes[1].legend(title='Churn', labels=['Not Churn', 'Churn'])

        plt.tight_layout()
        plt.show()


def plot_nonzero_hist_values(df, columns):
    for column in columns:
        non_zero_df = df[df[column] != 0]

        plot_histograms(non_zero_df, columns)


def plot_nonzero_hist_log_values(df, columns):
    for column in columns:
        non_zero_df = df[df[column] != 0]

        plot_log_histograms(non_zero_df, columns)



def plot_by_positive_negative(df, columns):
    df_copy = df.copy()
    for column in columns:
        # Podział wartości na dwie grupy: większe od zera i mniejsze od zera

        df_copy['is_positive'] = np.where(df_copy[column] > 0, 'Greater than zero',
                                               'Less than or equal to zero')

        # Wykres catplot
        sns.catplot(
            data=df_copy,
            x='is_positive',
            kind='count',
            col=column,
            # row='Churn',
            hue='Churn',
            aspect=1.5
        )
        plt.show()



