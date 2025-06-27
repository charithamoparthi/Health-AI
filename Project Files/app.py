import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os
from utils import init_granite_model, get_sample_patient_data, get_patient_profile

# Load environment variables
load_dotenv()

granite_model = init_granite_model()

# Streamlit App
st.set_page_config(page_title="HealthAI Assistant", layout="wide")
st.title("🩺 HealthAI: Your Personal Health Assistant")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["Patient Chat", "Disease Prediction", "Treatment Plan", "Health Analytics"])

# Sample data and patient profile
patient_profile = get_patient_profile()
patient_data = get_sample_patient_data()

# Ensure Date column is datetime
patient_data['Date'] = pd.to_datetime(patient_data['Date'])

# Patient Chat
if page == "Patient Chat":
    st.header("🔣️ Chat with HealthAI")
    st.markdown("Ask any health-related question. HealthAI will assist you.")

    user_query = st.text_input("Your question:", "What are the symptoms of high blood pressure?")
    if st.button("Ask HealthAI"):
        prompt = (
            f"You are a healthcare assistant. Answer the following question:\n"
            f"Question: {user_query}\nAnswer:"
        )
        response = granite_model.generate(prompt=prompt)
        st.markdown(response['results'][0]['generated_text'])

# Disease Prediction
elif page == "Disease Prediction":
    st.header("🧬 Disease Risk Assessment")
    st.markdown("Using your health metrics, we assess potential disease risks.")

    risk_prompt = (
        f"Based on the following patient data, list possible disease risks:\n"
        f"Age: {patient_profile['age']}\n"
        f"Gender: {patient_profile['gender']}\n"
        f"Medical History: {patient_profile['medical_history']}\n"
        f"Recent Vitals:\n{patient_data.tail(3).to_string(index=False)}\n\nAssessment:"
    )

    if st.button("Generate Risk Assessment"):
        response = granite_model.generate(prompt=risk_prompt)
        st.markdown(response['results'][0]['generated_text'])

# Treatment Plan
elif page == "Treatment Plan":
    st.header("💊 Personalized Treatment Plan")
    st.markdown("Get a suggested treatment approach based on your condition.")

    condition = st.text_input("Enter a condition:", "Hypertension")
    if st.button("Get Treatment Plan"):
        plan_prompt = (
            f"Provide a detailed yet easy-to-understand treatment plan for {condition} in a patient who is "
            f"{patient_profile['age']} years old {patient_profile['gender']} with this history: {patient_profile['medical_history']}"
        )
        response = granite_model.generate(prompt=plan_prompt)
        st.markdown(response['results'][0]['generated_text'])

# Health Analytics
elif page == "Health Analytics":
    st.header("📊 Health Metrics Analytics")
    st.markdown("Visualize and analyze your past health metrics.")

    st.subheader("Heart Rate Over Time")
    fig_hr = px.line(patient_data, x='Date', y='Heart Rate', title='Heart Rate Trend')
    st.plotly_chart(fig_hr, use_container_width=True)

    st.subheader("Blood Pressure Over Time")
    fig_bp = px.line(patient_data, x='Date', y=['Systolic BP', 'Diastolic BP'], title='Blood Pressure Trend')
    st.plotly_chart(fig_bp, use_container_width=True)

    st.subheader("Blood Glucose Over Time")
    fig_bg = px.line(patient_data, x='Date', y='Blood Glucose', title='Blood Glucose Trend')

    # Add a reference line for normal blood glucose range
    fig_bg.add_shape(
        type="line",
        x0=patient_data['Date'].min(),
        x1=patient_data['Date'].max(),
        y0=100,
        y1=100,
        line=dict(color="Red", dash="dot"),
    )
    fig_bg.add_annotation(
        x=patient_data['Date'].iloc[-1],
        y=100,
        text="Normal Max (Fasting)",
        showarrow=False,
        yshift=10
    )

    st.plotly_chart(fig_bg, use_container_width=True)

    # Provide text summary based on latest data
    st.subheader("Latest Summary")
    latest = patient_data.iloc[-1]
    previous_bg = patient_data['Blood Glucose'].iloc[-2] if len(patient_data) > 1 else latest['Blood Glucose']

    summary_prompt = (
        f"Summarize the following latest patient vitals and highlight any concerns:\n"
        f"Date: {latest['Date'].strftime('%Y-%m-%d')}\n"
        f"Heart Rate: {latest['Heart Rate']} bpm\n"
        f"Blood Pressure: {latest['Systolic BP']}/{latest['Diastolic BP']} mmHg\n"
        f"Blood Glucose: {latest['Blood Glucose']} mg/dL\n"
        f"Previous Blood Glucose: {previous_bg} mg/dL"
    )

    if st.button("Summarize Metrics"):
        response = granite_model.generate(prompt=summary_prompt)
        st.markdown(response['results'][0]['generated_text'])
