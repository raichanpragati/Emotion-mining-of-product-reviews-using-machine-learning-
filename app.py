import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('Sentiment_Analyser')
vectorizer = joblib.load('vectorizer.pkl')  # assuming you saved it during training

st.title('Sentiment Analyser')

ip = st.text_input('Enter your review: ')

if st.button('Predict'):
    if ip:
        # Transform the input text
        ip_vector = vectorizer.transform([ip])

        # Make prediction
        op = model.predict(ip_vector)
        ans = op[0]

        # Display result
        if ans == 'Positive':
            st.success("Positive 😊")
        elif ans == 'Negative':
            st.error("Negative 😞")
        elif ans == 'Neutral':
            st.warning("Neutral 😐")
        else:
            st.info(f"Predicted: {ans}")
    else:
        st.warning("Please enter a review to predict.")
