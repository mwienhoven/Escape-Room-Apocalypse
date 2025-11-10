import streamlit as st

PASSWORD = "mijnwachtwoord"


def login():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        user_input = st.text_input("Voer het wachtwoord in:", type="password")
        if st.button("Inloggen"):
            if user_input == PASSWORD:
                st.session_state.authenticated = True
                st.success("Succesvol ingelogd!")
            else:
                st.error("Wachtwoord incorrect!")
    return st.session_state.get("authenticated", False)
