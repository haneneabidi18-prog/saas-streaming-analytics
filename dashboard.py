import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Streaming Analytics SaaS", layout="wide")

st.title("📊 Streaming Analytics PRO Dashboard")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # ---------------- FILTERS ----------------
    st.sidebar.header("Filters")

    region_filter = st.sidebar.multiselect(
        "Region",
        df["region"].unique(),
        default=df["region"].unique()
    )

    device_filter = st.sidebar.multiselect(
        "Device",
        df["device"].unique(),
        default=df["device"].unique()
    )

    cdn_filter = st.sidebar.multiselect(
        "CDN",
        df["cdn"].unique(),
        default=df["cdn"].unique()
    )

    df_filtered = df[
        (df["region"].isin(region_filter)) &
        (df["device"].isin(device_filter)) &
        (df["cdn"].isin(cdn_filter))
    ]

    # ---------------- KPI ----------------
    avg_latency = df_filtered["latency"].mean()
    max_latency = df_filtered["latency"].max()
    avg_bitrate = df_filtered["bitrate"].mean()
    error_rate = (df_filtered["status"] != 200).mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("⚡ Avg Latency", f"{avg_latency:.2f}")
    col2.metric("🚀 Max Latency", f"{max_latency}")
    col3.metric("📺 Avg Bitrate", f"{avg_bitrate:.2f}")
    col4.metric("❌ Error Rate", f"{error_rate:.2%}")

    st.divider()

    # ---------------- AI INSIGHTS ----------------
    st.subheader("💡 AI Recommendations")

    recommendations = []

    if avg_latency > 400:
        recommendations.append("⚠️ Critical latency issue → optimize routing / CDN")

    if error_rate > 0.15:
        recommendations.append("❌ High error rate → possible outage or server issue")

    if avg_bitrate < 2000:
        recommendations.append("📉 Low bitrate → poor QoE")

    if avg_bitrate > 3800:
        recommendations.append("💰 Bitrate too high → cost optimization possible")

    if recommendations:
        for r in recommendations:
            st.warning(r)
    else:
        st.success("✅ System performance is optimal")

    st.divider()

    # ---------------- CHARTS ----------------
    st.subheader("📉 Latency Over Time")
    fig1 = px.line(df_filtered, x="timestamp", y="latency")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📺 Bitrate Over Time")
    fig2 = px.line(df_filtered, x="timestamp", y="bitrate")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("⚠️ Error Distribution")
    fig3 = px.histogram(df_filtered, x="status")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("🌍 Latency by Region")
    fig4 = px.box(df_filtered, x="region", y="latency")
    st.plotly_chart(fig4, use_container_width=True)

    st.divider()

    # ---------------- DATA ----------------
    st.subheader("📁 Filtered Data")
    st.dataframe(df_filtered.head(1000))

else:
    st.info("👆 Upload a CSV file to start analysis")