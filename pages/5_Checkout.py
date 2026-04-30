import streamlit as st

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login.")
    st.stop()

st.set_page_config(page_title="Checkout", layout="centered")

st.title("💳 Secure Checkout")
st.caption("Stripe payment simulation for demo purposes")

checkout_plan = st.session_state.get("checkout_plan", "pro")

if checkout_plan != "pro":
    st.warning("No plan selected.")
    st.stop()

st.subheader("Order Summary")

st.markdown("""
**Plan:** Pro  
**Price:** €29 / month  
**Billing:** Monthly  
""")

st.divider()

st.subheader("Payment Details")

with st.form("fake_payment_form"):
    name = st.text_input("Name on card")
    email = st.text_input("Billing email")
    card_number = st.text_input("Card number", placeholder="4242 4242 4242 4242")
    expiry = st.text_input("Expiry date", placeholder="12/28")
    cvc = st.text_input("CVC", placeholder="123", type="password")

    submitted = st.form_submit_button("Pay €29 and Upgrade")

if submitted:
    if not name or not email or not card_number or not expiry or not cvc:
        st.error("Please fill in all payment fields.")
    else:
        st.session_state["plan"] = "pro"
        st.success("Payment successful. Your account is now Pro.")
        st.balloons()

        st.markdown("""
        You can now access:
        - Save analysis history
        - Export executive PDF reports
        - Advanced insights
        """)

        if st.button("Go to Dashboard"):
            st.switch_page("pages/2_Dashboard.py")

import time

if submitted:
    with st.spinner("Processing payment..."):
        time.sleep(2)