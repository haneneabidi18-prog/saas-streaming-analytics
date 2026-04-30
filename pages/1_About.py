import streamlit as st

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login.")
    st.stop()

st.set_page_config(page_title="About", layout="wide")

st.title("OTT Revenue & Streaming Intelligence Platform")

st.markdown("""
### Turn streaming data into revenue, retention and executive decisions.

Streaming Analytics SaaS helps **OTT platforms, broadcasters and telecom operators**
understand content performance, user behavior and business impact from streaming data.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Revenue Intelligence")
    st.markdown("""
    Identify which content, countries and platforms generate the most value.

    - Revenue by country
    - Revenue per view
    - Top content performance
    - Monetization insights
    """)

with col2:
    st.subheader("Content Performance")
    st.markdown("""
    Understand what drives audience engagement.

    - Views by content
    - Watch time analysis
    - Device/platform usage
    - Performance trends
    """)

with col3:
    st.subheader("Executive Reporting")
    st.markdown("""
    Generate business-ready insights and reports.

    - Executive insights
    - PDF reports
    - Saved history
    - Pro analytics workflow
    """)

st.divider()

st.header("Built for OTT, Media and Telecom Teams")

st.markdown("""
This platform is designed for teams that need to make fast decisions from streaming data:

- OTT product teams
- Media groups
- Telecom operators
- Content distribution teams
- Business and revenue managers
- Data and analytics teams
""")

st.divider()

st.header("Why this product is different")

st.markdown("""
Generic analytics tools show dashboards.

This platform focuses on **streaming business intelligence**:

- Which content creates the most value?
- Which country generates the most revenue?
- Which device or platform drives engagement?
- What should executives focus on this week?
- Which reports can be shared with management or partners?
""")

st.divider()

st.header("Premium Features")

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    ### Free

    - CSV upload
    - Basic KPIs
    - Dashboard visualization
    - Filters by country, platform and content
    """)

with col5:
    st.markdown("""
    ### Pro

    - Save analysis history
    - Export executive PDF reports
    - Executive insights
    - Business-ready recommendations
    - Premium workflow for decision makers
    """)

st.divider()

st.header("Ideal use cases")

st.markdown("""
### For OTT platforms
Track content performance, engagement and revenue contribution.

### For telecom operators
Analyze bundle performance, device usage and market-level monetization.

### For media groups
Generate executive reports and identify top-performing content.

### For consultants
Deliver fast, professional analytics reports to clients.
""")

st.divider()

st.success("Ready to unlock premium insights? Go to the Pricing page and upgrade to Pro.")