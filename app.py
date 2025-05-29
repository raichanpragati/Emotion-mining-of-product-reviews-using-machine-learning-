

        # Display with emoji
import streamlit as st
import joblib
from PIL import Image

# Page config
st.set_page_config(page_title="Sentiment Analyser 🎭", page_icon="🎭", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .title {
            color: #2c3e50;
            font-size: 40px;
            text-align: center;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            color: #888;
            padding-top: 20px;
        }
        .prediction {
            font-size: 28px;
            text-align: center;
            color: #2ecc71;
            font-weight: bold;
        }
        .warning {
            font-size: 18px;
            color: #e74c3c;
        }
    </style>
""", unsafe_allow_html=True)

# Load trained model
model = joblib.load('Sentiment_Analyser')

# Title and description
st.markdown('<p class="title">🎭 Sentiment Analyser</p>', unsafe_allow_html=True)
st.markdown("##### 📊 Analyze customer reviews and see if they're **Positive**, **Negative**, or **Neutral** instantly!")

# Input field
ip = st.text_input('💬 Enter your product review here:')

# Predict button
if st.button('🔍 Predict Sentiment'):
    if ip.strip() != "":
        # Predict using the pipeline
        op = model.predict([ip])
        ans = op[0]

        # Emoji mapping
        emoji_dict = {
            'positive': '😊👍',
            'negative': '😞👎',
            'neutral': '😐'
        }

        emoji = emoji_dict.get(ans.lower(), '🤔')

        # Display prediction
        st.markdown(f'<p class="prediction">✨ Prediction: {ans.capitalize()} {emoji}</p>', unsafe_allow_html=True)

    else:
        st.markdown('<p class="warning">⚠️ Please enter a review to predict.</p>', unsafe_allow_html=True)

# Footer
#st.markdown('<p class="footer">Made with ❤️ by Pragati Rai</p>', unsafe_allow_html=True)
st.markdown("""
    <style>
        .footer {
            text-align: center;
            color: #888;
            padding-top: 20px;
            font-size: 16px;
        }
        .footer span {
            color: #e25555;
            font-size: 18px;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        .footer a {
            color: #f63366;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>

    <p class="footer">Made with <span>❤️</span> by <a href="https://www.linkedin.com/in/pragati-rai-518209237/" target="_blank">Pragati Rai</a></p>
""", unsafe_allow_html=True)
