import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streaming Analytics Dashboard", layout="wide")

st.title("📊 Streaming Analytics SaaS MVP")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    avg_latency = df["latency"].mean()
    max_latency = df["latency"].max()
    avg_bitrate = df["bitrate"].mean()
    error_rate = (df["status"] != 200).mean()

    st.subheader("📈 KPIs")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Avg Latency", round(avg_latency, 2))
    col2.metric("Max Latency", max_latency)
    col3.metric("Avg Bitrate", round(avg_bitrate, 2))
    col4.metric("Error Rate", round(error_rate, 2))

    st.subheader("📉 Charts")

    st.line_chart(df["latency"])
    st.line_chart(df["bitrate"])