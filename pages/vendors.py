import streamlit as st

from functools import reduce
from models.vendor import Vendor


# Store a session variable
if 'vendors_list' not in st.session_state:
    st.session_state.vendors_list = []

st.title("Add vendor")

col1, col2, col3 = st.columns(3)
with col1:
    name_input = st.text_input(label="Name")

with col2:
    phone_input = st.number_input(label="Phone", value=None, format=None, step=1)

with col3:
    website_input = st.text_input(label="Website")


vendors = []

if st.button("Save vendor"):
    try:   
        vendor = Vendor(name_input, phone_input, website_input)
        st.session_state.vendors_list.append(vendor)
        
    except ValueError as e:
        st.error(e)

for vendor in st.session_state.vendors_list:
    vendors.append({
        "Name": vendor.name,
        "Phone": vendor.phone,
        "Website": vendor.website
    })

st.header("Vendors")

st.data_editor(vendors, use_container_width=True, num_rows='dynamic')