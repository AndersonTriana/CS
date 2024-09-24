import streamlit as st

from models.product import Product
from models.client import Client
from models.vendor import Vendor
from models.inventory import Inventory

def load_initial_data():
    if 'products_list' not in st.session_state:
        st.session_state.products_list = [
            Product("Product A", 10.99, 100),
            Product("Product B", 5.49, 50),
            Product("Product C", 20.00, 30)
        ]

    if 'clients_list' not in st.session_state:
        st.session_state.clients_list = [
            Client("Client 1", 3132321232),
            Client("Client 2", 3132321232),
            Client("Client 3", 3132321232)
        ]

    if 'vendors_list' not in st.session_state:
        st.session_state.vendors_list = [
            Vendor("Provider A", 3132321232, "contact1@example.com"),
            Vendor("Provider B", 3132321232, "contact2@example.com")
        ]

load_initial_data()

def load_inventory():
    if 'inventory' not in st.session_state:
        st.session_state.inventory = Inventory()
        
        for product in st.session_state.products_list:
            st.session_state.inventory.add_product(product, 4)

load_inventory()

st.title("home")