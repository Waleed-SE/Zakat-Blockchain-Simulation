"""
Streamlit Zakat Blockchain Simulation App
Author: [Your Name]
Date: August 31, 2025

This app provides a web interface for the Zakat Blockchain Simulation.
"""
import streamlit as st
import time
from zakat_blockchain import Node, GLOBAL_BLOCKCHAIN

st.title("Zakat Blockchain Simulation")
st.write("Each student acts as a node. Zakat (2.5%) is deducted and distributed via blockchain blocks.")

# Session state for nodes
if 'nodes' not in st.session_state:
    st.session_state['nodes'] = {}

st.sidebar.header("Add Student Node")
name = st.sidebar.text_input("Student Name")
roll_number = st.sidebar.text_input("Roll Number")
if st.sidebar.button("Add Node"):
    if name and roll_number:
        if roll_number not in st.session_state['nodes']:
            st.session_state['nodes'][roll_number] = Node(name, roll_number)
            st.success(f"Node {name} ({roll_number}) added.")
        else:
            st.warning("Node with this roll number already exists.")
    else:
        st.error("Please enter both name and roll number.")

st.header("Nodes List")
if st.session_state['nodes']:
    for rn, node in st.session_state['nodes'].items():
        st.write(f"{node.name} (Roll: {rn}) - Balance: {node.balance}")
else:
    st.info("No nodes added yet.")

st.header("Pay Zakat")
if len(st.session_state['nodes']) >= 2:
    sender_roll = st.selectbox("Sender", list(st.session_state['nodes'].keys()), key="sender")
    receiver_roll = st.selectbox("Receiver", [r for r in st.session_state['nodes'] if r != sender_roll], key="receiver")
    if st.button("Pay Zakat"):
        sender = st.session_state['nodes'][sender_roll]
        receiver = st.session_state['nodes'][receiver_roll]
        sender.pay_zakat(receiver)
        st.success(f"{sender.name} paid Zakat to {receiver.name}.")
else:
    st.info("Add at least two nodes to pay Zakat.")


st.header("Transaction History & Blockchain")
for rn, node in st.session_state['nodes'].items():
    with st.expander(f"{node.name} ({rn})"):
        st.subheader("Transaction History")
        if node.transaction_history:
            for tx in node.transaction_history:
                st.write(tx)
        else:
            st.write("No transactions yet.")


st.subheader("Validate Blockchain")
if st.button("Validate Blockchain"):
    valid = GLOBAL_BLOCKCHAIN.validate_chain()
    if valid:
        st.success("Blockchain is valid.")
    else:
        st.error("Blockchain is INVALID!")

st.subheader("Global Blockchain")
for block in GLOBAL_BLOCKCHAIN.chain:
    st.json({
        'index': block.index,
        'timestamp': block.timestamp,
        'transactions': block.transactions,
        'previous_hash': block.previous_hash,
        'hash': block.hash,
        'roll_number': block.roll_number
    })
