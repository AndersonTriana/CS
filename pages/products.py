import streamlit as st

from functools import reduce
from models.product import Product

# Store a session variable
if 'products_list' not in st.session_state:
    st.session_state.products_list = []

st.title("Add product")

col1, col2, col3 = st.columns(3)
with col1:
    name_input = st.text_input(label="Product name")

with col2:
    price_input = st.number_input(label="Suggested Price", step=1000)

with col3:
    stock_input = st.number_input(label="Stock", step=1)

products = []

if st.button("Save product"):
    try:   
        product = Product(name_input, price_input, stock_input)

        st.session_state.products_list.append(product)

    except ValueError as e:
        st.error(e)

for product in st.session_state.products_list:
    products.append({
        "Name": product.name,
        "Suggested price": product.suggested_price,
        "Stock": product.stock
    })

st.header("Products")

st.data_editor(products, use_container_width=True, num_rows='dynamic')