import streamlit as st

from functools import reduce
from models.purchase import Purchase


# Store a session variable
if 'purchases_list' not in st.session_state:
    st.session_state.purchases_list = []

st.title("Purchases")

purchases = []

for purchase in st.session_state.purchases_list:
    purchases.append({
        "Vendor": purchase.vendor,
        "Total price": purchase.total_price,
        "Date": purchase.date
    })

st.data_editor(purchases, use_container_width=True, num_rows='dynamic')