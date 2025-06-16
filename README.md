# ⚡ PowerGuardian – AI-Powered Energy Theft Detection System

PowerGuardian is a smart energy monitoring system that uses machine learning to identify suspicious electricity consumption patterns and flag potential thefts.

## 🚀 Features

- 🔍 ML-based detection of abnormal usage
- 📈 Time-series visualization of flagged data
- 📊 Feature importance insights
- 🧪 Trained on synthetic smart meter data
- 🖥️ Streamlit dashboard for interactive UI

## 🧠 How It Works

- Data is uploaded in CSV format (`smart_meter_data.csv`)
- Feature extraction is performed from timestamps and user ID
- A Random Forest classifier is trained on the fly
- The model predicts normal vs theft behavior
- Output is shown in summary tables and charts

## 📊 Dashboard Screenshot

![screenshot](screenshots/usage_plot.png)

## 📎 Dataset
- Simulated 30-day smart meter readings for 5 users (hourly). 5% data is marked as theft.