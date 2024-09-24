import streamlit as st

from functools import reduce
from models.sale import Sale
from models.product import Product


# Store session variables
if 'sales_list' not in st.session_state:
    st.session_state.sales_list = []

if 'sale_products_list' not in st.session_state:
    st.session_state.sale_products_list = []


st.title("Add sale")

col1, col2 = st.columns(2)
with col1:
    vendor_input = st.selectbox(label="Choose a vendor", options=[vendor.name for vendor in st.session_state.vendors_list])
with col2:
    date_input = st.date_input(label="Sale date")

st.header("Add product")

col1, col2, col3, col4 = st.columns(4)
with col1:
    product_name_input = st.selectbox(label="Choose a product", options=[product.name for product in st.session_state.products_list])

with col2:
    stock_input = st.number_input(label="Quantity", value=1, step=1)

with col3:
    unit_cost_input = st.number_input(label="Unit cost", step=1000)

with col4:
    value_paid = st.number_input(label="Value paid", step=1000)

products = []
total_price = 0

for product in st.session_state.sale_products_list:
    total_price += product.suggested_price * product.stock

if st.button("Add product"):
    try:   
        product = Product(product_name_input, unit_cost_input, stock_input)
        product_stock = st.session_state.inventory.get_product_stock(product.name)

        for product_data in st.session_state.sale_products_list:
            if product_data.name == product.name:
                product_stock -= product.stock

        if product_stock >= product.stock:
            st.session_state.sale_products_list.append(product)
            
            for product in st.session_state.sale_products_list:
                total_price += product.suggested_price * product.stock
        else:
            if product_stock < 0: product_stock = 0
            raise ValueError(f"There are not enough units available for {product.name}. There are {product_stock} left")

    except ValueError as e:
        st.error(e)

for product in st.session_state.sale_products_list:
    products.append({
        "Name": product.name,
        "Unit cost": product.suggested_price,
        "Value paid": value_paid,
        "Quantity": product.stock,
        "Product": product,
        "Total cost": product.suggested_price * product.stock
    })

st.data_editor(products, use_container_width=True, num_rows='dynamic', column_order=['Name', 'Quantity', 'Unit cost', 'Total cost', 'Value paid'])

col1, col2 = st.columns(2)

with col1:
    if st.button("Save sale"):
        try:   
            sale = Sale(vendor_input, date_input)
            for product in products:
                sale.add_product(product["Product"], product["Quantity"], product["Unit cost"], product["Value paid"])
            
            st.session_state.sales_list.append(sale)
            
            for product in st.session_state.sale_products_list:
                st.session_state.inventory.update_stock(product.name, st.session_state.inventory.get_product_stock(product.name) - product.stock)
            
            st.session_state.sale_products_list = []
            
            st.switch_page("pages/sales.py")
            
        except ValueError as e:
            st.error(e)

with col2:
    st.metric("Total price", total_price)