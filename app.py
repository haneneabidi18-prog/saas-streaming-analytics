import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title="Streaming Analytics SaaS",
    page_icon="📊",
    layout="wide"
)

# Load authentication config
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"]
)

# Login form
authenticator.login(location="main")

# Get login state
name = st.session_state.get("name")
authentication_status = st.session_state.get("authentication_status")
username = st.session_state.get("username")

# Authentication logic
if authentication_status:
    authenticator.logout(location="sidebar")

    # User plan management
    if "plan" not in st.session_state:
        st.session_state["plan"] = "pro"

    st.sidebar.success(f"Logged in as {name}")
    st.sidebar.info(f"Current plan: {st.session_state['plan'].upper()}")

    st.title("📊 Streaming Analytics SaaS")
    st.subheader("Premium analytics platform for OTT, media and telecom businesses")

    st.markdown("""
    Welcome to your premium SaaS dashboard.

    Use the sidebar to navigate:
    - About
    - Dashboard
    - History
    - Pricing
    """)

    st.info("Start by opening the Dashboard page from the sidebar.")

elif authentication_status is False:
    st.error("Username or password is incorrect")

else:
    st.warning("Please enter your username and password")