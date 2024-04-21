import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Profits",
)
st.sidebar.header("Profits analysis")
st.title('Cell2Cell Case')

data = pd.read_csv('../data/telecom/cell2celltrain.csv')
# st.dataframe(data)
st.write(data[['Churn', 'MonthlyRevenue', 'MonthlyMinutes', 'MonthsInService', 'ServiceArea']].describe())
st.write('Let\'s analyze potential savings of Cell2Cell company')
customer_acquirement_cost = st.number_input('Customer Acquisition Cost', value=200) # między 150 a 300!
cost_of_retention = st.number_input('Retention offer cost', value=20)
retention_stats = data[data['RetentionCalls'] > 0]['RetentionOffersAccepted']
retention_success_rate = retention_stats[retention_stats > 0].count() / len(retention_stats) # 0.5
churned = data[data['Churn'] == 'Yes']
normal_cost = customer_acquirement_cost * churned['Churn'].count()
our_cost = (retention_success_rate * churned['Churn'].count()) * customer_acquirement_cost + ((1-retention_success_rate) * churned['Churn'].count() * cost_of_retention)


if 'saving_header' not in st.session_state:
    st.session_state.saving_header = False
def show_saving_header():
    st.session_state.saving_header = True

st.button("Calculate offer", on_click=show_saving_header)
if st.session_state.saving_header:
    st.header(f"You can save :red[\${normal_cost - our_cost:.2f}] with us.")