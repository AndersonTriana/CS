import streamlit as st

from functools import reduce
from models.sale import Sale


# Store a session variable
if 'sales_list' not in st.session_state:
    st.session_state.sales_list = []

st.title("Sales")

sales = []

for sale in st.session_state.sales_list:
    sales.append({
        "Client": sale.client,
        "Total price": sale.total_price,
        "Value paid": sale.total_paid,
        "Date": sale.date
    })

st.data_editor(sales, use_container_width=True, num_rows='dynamic')