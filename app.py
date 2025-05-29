
import streamlit as st
import joblib
import plotly.express as px

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('Sentiment_Analyser.pkl')

model = load_model()

# Track prediction counts
if 'prediction_counts' not in st.session_state:
    st.session_state.prediction_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

# App Title & Description
st.markdown("""
    <h1 style="text-align:center; color: #ff4b4b;">✨🎉 Product Review Sentiment Analyser 🎉✨</h1>
    <h4 style="text-align:center; color: gray;">🔍 Analyse your product review emotions with a click! 💬❤️😢</h4>
    <hr style="border: 1px solid #f63366;">
""", unsafe_allow_html=True)

# User Input
ip = st.text_input("📝 Enter your product review:")

# Predict button
if st.button("🔮 Predict Sentiment"):
    if ip:
        try:
            op = model.predict([ip])
            prediction = op[0]

            # Display sentiment with emoji
            if prediction.lower() == 'positive':
                st.success(f"✅ Sentiment: **Positive** 😍🎉")
                st.session_state.prediction_counts['Positive'] += 1
            elif prediction.lower() == 'negative':
                st.error(f"❌ Sentiment: **Negative** 😡👎")
                st.session_state.prediction_counts['Negative'] += 1
            else:
                st.warning(f"⚠️ Sentiment: **Neutral** 😐")
                st.session_state.prediction_counts['Neutral'] += 1

        except Exception as e:
            st.error(f"❌ Error while predicting: {e}")
    else:
        st.warning("⚠️ Please enter a review to predict.")

# Draw sentiment pie chart
sentiments = list(st.session_state.prediction_counts.keys())
counts = list(st.session_state.prediction_counts.values())

fig = px.pie(
    values=counts,
    names=sentiments,
    color=sentiments,
    color_discrete_map={'Positive':'#00cc96','Negative':'#ff4b4b','Neutral':'#636efa'},
    title="📊 Sentiment Prediction Summary"
)

st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("""
    <hr>
    <p style="text-align:center; color: #888;">Made with ❤️ by Pragati</p>
""", unsafe_allow_html=True)
