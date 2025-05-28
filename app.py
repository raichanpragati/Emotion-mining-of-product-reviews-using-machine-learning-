import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words('english')

REPLACE_BY_SPACE_RE = re.compile('[/(){}—\[\]|@,;‘?|।!–’-]')

def clean_text(sample):
    if not isinstance(sample, str):
        return ""
    sample = sample.lower()
    sample = sample.replace("<br /><br />", "")
    sample = REPLACE_BY_SPACE_RE.sub(' ', sample)
    sample = re.sub("[^a-z]+", " ", sample)
    sample = sample.split()
    sample = [word for word in sample if word not in stop_words]
    return " ".join(sample)

# Load the trained model once here
model = joblib.load('Sentiment_Analyser.pkl')

st.title('Sentiment Analyser 🎭')

ip = st.text_input('Enter your review:')

if st.button('Predict'):
    if ip.strip() != "":
        cleaned_ip = clean_text(ip)
        prediction = model.predict([cleaned_ip])
        st.subheader(f"Prediction: {prediction[0]}")
    else:
        st.warning("Please enter a review to predict.")
