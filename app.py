import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard")

st.title("📈 Sales Forecasting & Business Analytics Dashboard")

df = pd.read_csv("sales_data.csv")

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
highest_sales = df["Sales"].max()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Average Sales", f"₹{average_sales:,.0f}")
col3.metric("Highest Monthly Sales", f"₹{highest_sales:,.0f}")

st.subheader("Monthly Sales Trend")

fig = px.line(df, x="Month", y="Sales", markers=True)

st.plotly_chart(fig)

forecast = average_sales * 1.05

st.subheader("Sales Forecast")

st.success(f"Expected Next Month Sales: ₹{forecast:,.0f}")

st.subheader("Business Insights")

st.write("• Sales show an overall upward trend throughout the year.")
st.write("• December recorded the highest sales performance.")
st.write("• Forecast indicates continued business growth.")