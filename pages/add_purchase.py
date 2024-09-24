import streamlit as st

from functools import reduce
from models.purchase import Purchase
from models.product import Product


# Store session variables
if 'purchases_list' not in st.session_state:
    st.session_state.purchases_list = []

if 'purchase_products_list' not in st.session_state:
    st.session_state.purchase_products_list = []

st.title("Add purchase")

col1, col2 = st.columns(2)
with col1:
    vendor_input = st.selectbox(label="Choose a vendor", options=[vendor.name for vendor in st.session_state.vendors_list])
with col2:
    date_input = st.date_input(label="Purchase date")

st.header("Add product")

col1, col2, col3 = st.columns(3)
with col1:
    product_name_input = st.selectbox(label="Choose a product", options=[product.name for product in st.session_state.products_list])

with col2:
    unit_cost_input = st.number_input(label="Unit cost", step=1000)

with col3:
    stock_input = st.number_input(label="Quantity", value=1, step=1)

products = []

if st.button("Add product"):
    try:   
        product = Product(product_name_input, unit_cost_input, stock_input)

        st.session_state.purchase_products_list.append(product)

    except ValueError as e:
        st.error(e)

for product in st.session_state.purchase_products_list:
    products.append({
        "Name": product.name,
        "Unit cost": product.suggested_price,
        "Quantity": product.stock,
        "Product": product,
        "Total cost": product.suggested_price * product.stock
    })

st.data_editor(products, use_container_width=True, num_rows='dynamic', column_order=['Name', 'Quantity', 'Unit cost', 'Total cost'])

if st.button("Save purchase"):
    try:   
        purchase = Purchase(vendor_input, date_input)
        for product in products:
            purchase.add_product(product["Product"], product["Quantity"], product["Unit cost"])
        
        purchase.calculate_total_price();
        
        st.session_state.purchases_list.append(purchase)
        
        for product in st.session_state.purchase_products_list:
            st.write(product)
            st.session_state.inventory.update_stock(product.name, st.session_state.inventory.get_product_stock(product.name) + product.stock)
        
        st.session_state.purchase_products_list = []
        
        st.switch_page("pages/purchases.py")
        
    except ValueError as e:
        st.error(e)