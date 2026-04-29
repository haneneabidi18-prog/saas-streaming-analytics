import streamlit as st

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login from the home page.")
    st.stop()
    
import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.title("About / Value Proposition")

st.markdown("""
## Streaming Analytics SaaS

Streaming Analytics SaaS helps **OTT platforms, media groups and telecom operators**
understand their streaming performance from CSV or live data.

### Value proposition

This platform helps business and technical teams to:

- Analyze content performance
- Understand user behavior
- Track views, watch time and revenue
- Identify top-performing platforms and countries
- Support monetization decisions
- Prepare future API-based analytics

### Ideal customers

- OTT platforms
- Media companies
- Telecom operators
- Content distributors
- Digital product teams

### Premium features coming soon

- User login
- Saved history
- Live API integration
- Multi-user workspace
- Business dashboards
""")