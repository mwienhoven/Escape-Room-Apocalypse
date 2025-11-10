import streamlit as st
from src.hex_converter import decimal_to_hex


def show_converter():
    st.title("Hexadecimale Converter")

    decimal_number = st.number_input("Voer een decimaal getal in:", min_value=0, step=1)

    if st.button("Converteer naar hexadecimaal"):
        hex_number = decimal_to_hex(decimal_number)
        st.write(f"Hexadecimaal: {hex_number}")
