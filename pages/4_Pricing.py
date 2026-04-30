import streamlit as st

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login.")
    st.stop()

st.set_page_config(page_title="Pricing", layout="wide")

st.title("💎 Pricing Plans")
st.markdown("### Choose the plan that fits your business needs")

current_plan = st.session_state.get("plan", "free")

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
            st.session_state["checkout_plan"] = "pro"
            st.switch_page("pages/5_Checkout.py")

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