
import streamlit as st
import joblib

# Load your trained pipeline (vectorizer + model inside)
model = joblib.load('Sentiment_Analyser.pkl')

# Streamlit UI
st.title('Sentiment Analyser 🎭')

ip = st.text_input('Enter your review:')

if st.button('Predict'):
    if ip.strip() != "":
        # Directly predict using the pipeline
        op = model.predict([ip])
        ans = op[0]

        # Display with emoji
        st.subheader(f"Prediction: {ans}")
    else:
        st.warning("Please enter a review to predict.")
