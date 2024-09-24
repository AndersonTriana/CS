import streamlit as st

from functools import reduce
from models.client import Client

# Store a session variable
if 'clients_list' not in st.session_state:
    st.session_state.clients_list = []

st.title("Add client")

col1, col2 = st.columns(2)
with col1:
    name_input = st.text_input(label="Name")

with col2:
    phone_input = st.number_input(label="Phone", value=None, format=None, step=1)


clients = []

if st.button("Save client"):
    try:   
        client = Client(name_input, phone_input)
        st.session_state.clients_list.append(client)
        
    except ValueError as e:
        st.error(e)

for client in st.session_state.clients_list:
    clients.append({
        "Name": client.name,
        "Phone": client.phone
    })

st.header("Clients")

st.data_editor(clients, use_container_width=True, num_rows='dynamic')