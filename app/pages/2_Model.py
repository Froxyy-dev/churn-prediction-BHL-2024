import streamlit as st
import pandas as pd
import pickle


def load_model_from_pickle(filename='final_model.pkl'):
    # Load the trained model from the pickle file
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model


def add_section(title):
    st.markdown(f'## {title}')


def add_write(title):
    st.write(f'{title}')


def add_text(text):
    st.write(text)


def add_table(data):
    st.write(data)


def add_image(image_url, caption=None, width=None):
    st.image(image_url, caption=caption, use_column_width=width)


def add_code(code, language='python'):
    st.code(code, language=language)


import numpy as np


def get_most_certain_predictions(model, X_test):
    # Get probabilities for each class

    X_test = X_test.dropna()
    probabilities = model.predict_proba(X_test)

    # Find the maximum probability for class 1 and class 0
    max_probabilities_class_1 = np.max(probabilities[:, 1])
    max_probabilities_class_0 = np.max(probabilities[:, 0])

    # Find indices for the most certain predictions for class 1 and class 0
    index_most_certain_class_1 = np.where(probabilities[:, 1] == max_probabilities_class_1)[0][0]
    index_most_certain_class_0 = np.where(probabilities[:, 0] == max_probabilities_class_0)[0][0]

    # Extract the most certain samples for class 1 and class 0 from X_test
    most_certain_samples_class_1 = X_test.iloc[index_most_certain_class_1]
    most_certain_samples_class_0 = X_test.iloc[index_most_certain_class_0]

    feature_importance = model.feature_importances_
    sorted_idx = np.argsort(feature_importance)
    ten_most_important_features = X_test.columns[sorted_idx][-10:]
    ten_most_important_features.drop('PercChangeRevenues')

    filtered_1 = most_certain_samples_class_1[ten_most_important_features]
    filtered_0 = most_certain_samples_class_0[ten_most_important_features]

    return filtered_0, filtered_1


def data_visualization_page_by_wojtek():
    st.set_page_config(
        page_title="Model in action",
    )
    st.title('Model in action')
    add_section("Let's see our model in action")
    add_write("Our app loads model, data and predict which customer is likely to churn.")
    add_write("Let's see what characterized those customers.")
    add_section("\n")

    final_model_unpacked = load_model_from_pickle()
    test_data = pd.read_csv('data.csv')

    add_write("Statistics of low-churn-risk client (left) vs high-churn-risk one:")
    sure_loyal_client, sure_churn_client = get_most_certain_predictions(final_model_unpacked, test_data)
    clients_df = sure_loyal_client.to_frame().join(sure_churn_client)
    st.dataframe(clients_df)

    add_text("\n")
    add_write("In fact our model takes over 50 parameters, but above 10 were considered to be the most important.")
    add_write("Let us see in more details what parameters are important:")
    add_image('important.png')

data_visualization_page_by_wojtek()