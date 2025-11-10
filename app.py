import streamlit as st
from src.auth import login
from tabs.converter_tab import show_converter

# --- Login check ---
if login():
    show_converter()
