# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="⚡ PowerGuardian", layout="wide")

st.title("⚡ PowerGuardian – Energy Theft Detection Dashboard")
st.markdown("Upload smart meter CSV data and detect abnormal usage using Machine Learning.")

uploaded_file = st.file_uploader("📥 Upload smart_meter_data.csv", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["timestamp"])

    # Feature Engineering
    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.day
    df["weekday"] = df["timestamp"].dt.weekday
    le = LabelEncoder()
    df["user_id_encoded"] = le.fit_transform(df["user_id"])
    df["label_encoded"] = df["label"].map({"normal": 0, "theft": 1})

    X = df[["energy_usage_kWh", "hour", "day", "weekday", "user_id_encoded"]]
    y = df["label_encoded"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    df["prediction"] = model.predict(X)

    # Summary Table
    st.subheader("🔍 Prediction Table")
    st.dataframe(df[["timestamp", "user_id", "energy_usage_kWh", "label", "prediction"]].head(10))

    # Counts
    theft = (df["prediction"] == 1).sum()
    normal = (df["prediction"] == 0).sum()
    st.success(f"✅ Normal: {normal} | ⚠️ Theft: {theft}")

    # Energy Usage Plot
    st.subheader("📊 Energy Usage Over Time")
    plt.figure(figsize=(10, 4))
    df[df["prediction"] == 1].groupby("timestamp")["energy_usage_kWh"].mean().plot(label="Theft", color="red")
    df[df["prediction"] == 0].groupby("timestamp")["energy_usage_kWh"].mean().plot(label="Normal", color="green")
    plt.legend()
    plt.ylabel("Energy (kWh)")
    st.pyplot(plt)

    # Feature Importance
    st.subheader("📌 Feature Importance")
    feat_imp = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)
    st.bar_chart(feat_imp.set_index("Feature"))
