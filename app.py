import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="APL Logistics — Risk Dashboard",
    page_icon="🚚",
    layout="wide"
)

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mohankumawat17-bit/APL-Logistics-Risk-Prediction/main/risk_scores.csv"
    return pd.read_csv(url)

df = load_data()

# title
st.title("🚚 APL Logistics — Late Delivery Risk Dashboard")
st.markdown("---")

# top metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Orders", f"{len(df):,}")
with col2:
    st.metric("🟢 Low Risk", f"{len(df[df['Risk_Category'] == 'Low Risk']):,}")
with col3:
    st.metric("🟡 Medium Risk", f"{len(df[df['Risk_Category'] == 'Medium Risk']):,}")
with col4:
    st.metric("🔴 High Risk", f"{len(df[df['Risk_Category'] == 'High Risk']):,}")

st.markdown("---")

# section 1 - risk distribution
st.subheader("📊 Risk Distribution Overview")

col1, col2 = st.columns(2)

with col1:
    risk_counts = df['Risk_Category'].value_counts()
    colors_map = {'Low Risk': 'green', 'Medium Risk': 'orange', 'High Risk': 'red'}

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(risk_counts.index, risk_counts.values,
                  color=[colors_map[x] for x in risk_counts.index])
    for bar, count in zip(bars, risk_counts.values):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 100,
                f'{count:,}', ha='center', fontsize=10)
    ax.set_title('Orders by Risk Category')
    ax.set_ylabel('Number of Orders')
    st.pyplot(fig)

with col2:
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.pie(risk_counts.values,
            labels=risk_counts.index,
            colors=[colors_map[x] for x in risk_counts.index],
            autopct='%1.1f%%', startangle=90)
    ax2.set_title('Risk Category Breakdown')
    st.pyplot(fig2)

st.markdown("---")

# section 2 - feature importance image
st.subheader("🔍 What causes late delivery?")
feat_url = "https://raw.githubusercontent.com/mohankumawat17-bit/APL-Logistics-Risk-Prediction/main/feature_importance.png"
st.image(feat_url, use_container_width=True)

st.markdown("---")

# section 3 - high risk orders
st.subheader("🔴 High Risk Orders — Immediate Attention Required")
high_risk_df = df[df['Risk_Category'] == 'High Risk'].sort_values(
    'Late_Probability', ascending=False).reset_index(drop=True)
st.dataframe(high_risk_df.head(20), use_container_width=True)

st.markdown("---")

# section 4 - probability distribution
st.subheader("📈 Late Delivery Probability Distribution")
fig3, ax3 = plt.subplots(figsize=(10, 4))
ax3.hist(df['Late_Probability'], bins=50, color='steelblue', edgecolor='white')
ax3.axvline(x=0.4, color='orange', linestyle='--', label='Medium Risk threshold')
ax3.axvline(x=0.6, color='red', linestyle='--', label='High Risk threshold')
ax3.set_xlabel('Late Delivery Probability')
ax3.set_ylabel('Number of Orders')
ax3.set_title('Distribution of Risk Probabilities')
ax3.legend()
st.pyplot(fig3)

st.markdown("---")
st.caption("Built by Mohan Lal Kumawat | Unified Mentor Internship | APL Logistics Project")
