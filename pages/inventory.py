import streamlit as st

from functools import reduce
from models.product import Product

st.title("Inventory")

products = []

for product in st.session_state.inventory.products:
    products.append({
        "Product name": st.session_state.inventory.products[product]["product"].name,
        "Stock": st.session_state.inventory.products[product]["stock"],
        "Suggested price": st.session_state.inventory.products[product]["product"].suggested_price
    })

st.data_editor(products, use_container_width=True, num_rows='dynamic')