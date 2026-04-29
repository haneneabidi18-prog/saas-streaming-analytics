import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Streaming Analytics Dashboard")

st.markdown("Upload your streaming CSV file or download the sample file.")

sample_path = "sample_data/sample_streaming_data.csv"

if os.path.exists(sample_path):
    with open(sample_path, "rb") as file:
        st.download_button(
            label="⬇️ Download sample CSV",
            data=file,
            file_name="sample_streaming_data.csv",
            mime="text/csv"
        )

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Data Preview")
    st.dataframe(df)

    required_columns = ["views", "watch_time_minutes", "revenue"]

    if all(col in df.columns for col in required_columns):
        total_views = df["views"].sum()
        total_watch_time = df["watch_time_minutes"].sum()
        total_revenue = df["revenue"].sum()

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Views", f"{total_views:,}")
        col2.metric("Watch Time Minutes", f"{total_watch_time:,}")
        col3.metric("Revenue", f"€{total_revenue:,.2f}")

        if "platform" in df.columns:
            st.subheader("Views by Platform")
            fig = px.bar(
                df.groupby("platform")["views"].sum().reset_index(),
                x="platform",
                y="views",
                title="Views by Platform"
            )
            st.plotly_chart(fig, use_container_width=True)

        if "country" in df.columns:
            st.subheader("Revenue by Country")
            fig2 = px.pie(
                df.groupby("country")["revenue"].sum().reset_index(),
                names="country",
                values="revenue",
                title="Revenue by Country"
            )
            st.plotly_chart(fig2, use_container_width=True)

        if "content_title" in df.columns:
            st.subheader("Top Content")
            top_content = df.groupby("content_title")["views"].sum().reset_index()
            top_content = top_content.sort_values(by="views", ascending=False)
            st.dataframe(top_content)

    else:
        st.error("Your CSV must contain: views, watch_time_minutes, revenue")
else:
    st.warning("Please upload a CSV file to start.")