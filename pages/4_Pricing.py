import streamlit as st
import time

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login.")
    st.stop()

st.set_page_config(page_title="Pricing", layout="wide")

if "show_checkout" not in st.session_state:
    st.session_state["show_checkout"] = False

current_plan = st.session_state.get("plan", "free")

# CHECKOUT MODE
if st.session_state["show_checkout"]:
    st.title("💳 Secure Checkout")
    st.caption("Stripe payment simulation for demo purposes")

    st.subheader("Order Summary")
    st.markdown("""
    **Plan:** Pro  
    **Price:** €29 / month  
    **Billing:** Monthly  
    """)

    st.divider()

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
            with st.spinner("Processing payment..."):
                time.sleep(2)

            st.session_state["plan"] = "pro"
            st.session_state["show_checkout"] = False
            st.success("Payment successful. Your account is now Pro.")
            st.balloons()

    if st.button("Back to Pricing"):
        st.session_state["show_checkout"] = False
        st.rerun()

    st.stop()

# PRICING MODE
st.title("💎 Pricing Plans")
st.markdown("### Choose the plan that fits your business needs")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Free")
    st.markdown("""
    **€0 / month**

    ✔ Upload CSV  
    ✔ Basic dashboard  
    ✔ Standard KPIs  

    ❌ Save history  
    ❌ Export PDF  
    ❌ Advanced insights  
    """)

    if current_plan == "free":
        st.success("Current Plan")
    else:
        if st.button("Downgrade to Free"):
            st.session_state["plan"] = "free"
            st.success("Switched to Free")

with col2:
    st.subheader("Pro 🚀")
    st.markdown("""
    **€29 / month**

    ✔ Everything in Free  
    ✔ Save analysis history  
    ✔ Export executive PDF reports  
    ✔ Advanced insights  
    ✔ Business-ready analytics  

    👉 Perfect for OTT teams & analysts
    """)

    if current_plan == "pro":
        st.success("Current Plan")
    else:
        if st.button("Upgrade to Pro"):
            st.session_state["show_checkout"] = True
            st.rerun()

with col3:
    st.subheader("Enterprise 🏢")
    st.markdown("""
    **Custom pricing**

    ✔ Multi-user access  
    ✔ API integration  
    ✔ Live data pipelines  
    ✔ Custom dashboards  
    ✔ Dedicated support  

    👉 For telcos & media groups
    """)

    if st.button("Contact Sales"):
        st.info("A sales contact form will be added later.")

st.divider()

st.markdown("""
### Why upgrade?

- Turn data into actionable insights  
- Generate executive-ready reports  
- Track performance over time  
- Make data-driven business decisions  

🚀 Upgrade to Pro to unlock the full power of the platform.
""")