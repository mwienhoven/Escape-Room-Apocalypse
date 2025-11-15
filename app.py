import streamlit as st
import random
import string

# Data
CORRECT_ORDER = ["Marcello", "Julia", "Jesper", "Nardine", "Rik", "Kurt"]
SECRET_PASSWORD = "Noobie69ez"
NAMES = [
    "Kurt",
    "Marcello",
    "Jesper",
    "Nardine",
    "Julia",
    "Rik",
]


# Function to generate fake passwords
def generate_fake_password():
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(10))


st.title("Name Order Puzzle 🔐")

# --------------------
# PUZZLE SECTION
# --------------------
st.header("🔢 The Puzzle")
st.write(
    "Place all six names in the correct order. Every unique combination generates a password automatically."
)

# Dropdowns
positions = []
for i in range(6):
    choice = st.selectbox(
        f"Position {i+1}", ["-- select a name --"] + NAMES, key=f"position_{i}"
    )
    positions.append(choice)

st.write("---")

# PASSWORD LOGIC
if "-- select a name --" in positions:
    st.info("Fill in all positions to generate the password.")
    password = ""
else:
    if len(positions) != len(set(positions)):
        st.error("Each name must be used only once. No duplicates allowed.")
        password = ""
    else:
        if positions == CORRECT_ORDER:
            password = SECRET_PASSWORD
        else:
            password = generate_fake_password()

st.text_input("Generated Password:", value=password, disabled=True)

st.write("---")

# --------------------
# PASSWORD UNLOCK AREA
# --------------------
st.subheader("Enter the final password to unlock the reward:")

user_pw = st.text_input("Password:", type="password", key="unlock_pw")

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if st.button("Unlock"):
    if user_pw == SECRET_PASSWORD:
        st.session_state.unlocked = True
        st.balloons()
    else:
        st.error("Incorrect password. Try again.")


# --------------------
# UNLOCKED SCREEN → HEX CONVERTER
# --------------------
if st.session_state.unlocked:
    st.write("---")
    st.header("🔓 Reward: Hexadecimal Converter")

    # Text input zodat '191E' ook geldig is
    user_hex_input = st.text_input("Enter a number or hex value:")

    # Probeer om decimaal naar hex om te zetten
    hex_value = ""
    if user_hex_input != "":
        # Check of input puur numeriek is → dan omzetten naar hex
        if user_hex_input.isdigit():
            hex_value = hex(int(user_hex_input))[2:].upper()
        else:
            # Anders gewoon tonen wat is ingevuld
            hex_value = user_hex_input.upper()

    st.text_input("Hexadecimal Value:", value=hex_value, disabled=True)

    # SPECIAL CHECK: gebruiker tikt letterlijk 191E in
    if user_hex_input.upper() == "191E":
        st.success(
            "Marcello is de beste Oppergod die er bestaat en Hij zal ons helen! 🙌🔥"
        )
