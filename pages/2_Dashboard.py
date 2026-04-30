import streamlit as st

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login from the home page.")
    st.stop()

import pandas as pd
import plotly.express as px
import os
import json
from datetime import datetime

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Streaming Analytics PRO Dashboard")

# Download sample CSV
sample_path = "sample_data/sample_streaming_data.csv"

if os.path.exists(sample_path):
    with open(sample_path, "rb") as file:
        st.download_button(
            label="⬇️ Download sample CSV",
            data=file,
            file_name="sample_streaming_data.csv",
            mime="text/csv"
        )

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is None:
    st.info("👆 Upload a CSV file to start analysis")
    st.stop()

df = pd.read_csv(uploaded_file)
df.columns = df.columns.str.strip().str.lower()

st.success("CSV uploaded successfully!")

st.subheader("Data Preview")
st.dataframe(df, use_container_width=True)

# Required columns
required_columns = ["views", "watch_time_minutes", "revenue"]
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.write("Detected columns:", list(df.columns))
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")

filtered_df = df.copy()

if "country" in df.columns:
    countries = st.sidebar.multiselect(
        "Select country",
        options=sorted(df["country"].dropna().unique()),
        default=sorted(df["country"].dropna().unique())
    )
    filtered_df = filtered_df[filtered_df["country"].isin(countries)]

if "platform" in df.columns:
    platforms = st.sidebar.multiselect(
        "Select device / platform",
        options=sorted(df["platform"].dropna().unique()),
        default=sorted(df["platform"].dropna().unique())
    )
    filtered_df = filtered_df[filtered_df["platform"].isin(platforms)]

if "content_title" in df.columns:
    contents = st.sidebar.multiselect(
        "Select content",
        options=sorted(df["content_title"].dropna().unique()),
        default=sorted(df["content_title"].dropna().unique())
    )
    filtered_df = filtered_df[filtered_df["content_title"].isin(contents)]

# KPIs
total_views = filtered_df["views"].sum()
total_watch_time = filtered_df["watch_time_minutes"].sum()
total_revenue = filtered_df["revenue"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Views", f"{total_views:,}")
col2.metric("Watch Time Minutes", f"{total_watch_time:,}")
col3.metric("Revenue", f"€{total_revenue:,.2f}")

# Save Analysis
# Save Analysis - PRO feature
st.subheader("💾 Save Analysis")

if st.session_state.get("plan") == "free":

    if st.button("Save Analysis"):
        os.makedirs("storage", exist_ok=True)

        history_item = {
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": st.session_state.get("username", "unknown"),
            "total_views": int(total_views),
            "total_watch_time_minutes": int(total_watch_time),
            "total_revenue": float(total_revenue)
        }

        username = st.session_state.get("username", "unknown")
        file_path = f"storage/history_{username}.json"

        try:
            with open(file_path, "r") as file:
                history_data = json.load(file)
        except FileNotFoundError:
            history_data = []

        history_data.append(history_item)

        with open(file_path, "w") as file:
            json.dump(history_data, file, indent=2)

        st.success("Analysis saved successfully!")

else:
    st.warning("🔒 Save Analysis is a Pro feature. Upgrade to Pro to save your reports.")

st.divider()

# Charts
if "platform" in filtered_df.columns:
    st.subheader("Views by Device / Platform")
    platform_df = filtered_df.groupby("platform", as_index=False)["views"].sum()

    fig_platform = px.bar(
        platform_df,
        x="platform",
        y="views",
        title="Views by Device / Platform"
    )
    st.plotly_chart(fig_platform, use_container_width=True)

if "country" in filtered_df.columns:
    st.subheader("Revenue by Country")
    country_df = filtered_df.groupby("country", as_index=False)["revenue"].sum()

    fig_country = px.pie(
        country_df,
        names="country",
        values="revenue",
        title="Revenue by Country"
    )
    st.plotly_chart(fig_country, use_container_width=True)

if "content_title" in filtered_df.columns:
    st.subheader("Top Content by Views")

    top_content = (
        filtered_df.groupby("content_title", as_index=False)["views"]
        .sum()
        .sort_values(by="views", ascending=False)
    )

    fig_content = px.bar(
        top_content,
        x="content_title",
        y="views",
        title="Top Content by Views"
    )
    st.plotly_chart(fig_content, use_container_width=True)

    st.dataframe(top_content, use_container_width=True)

if "date" in filtered_df.columns:
    st.subheader("Views Evolution Over Time")

    filtered_df["date"] = pd.to_datetime(filtered_df["date"], errors="coerce")
    time_df = filtered_df.groupby("date", as_index=False)["views"].sum()

    fig_time = px.line(
        time_df,
        x="date",
        y="views",
        title="Views Over Time"
    )
    st.plotly_chart(fig_time, use_container_width=True)