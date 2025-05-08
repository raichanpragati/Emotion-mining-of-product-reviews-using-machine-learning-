import streamlit as st
import sklearn
import joblib

model = joblib.load('Sentiment_Analyser')
st.title('Sentiment Analyser')
ip = st.text_input('Enter your review: ')
#op = model.predict([ip])
#ans=op[0]
if st.button('Predict'):
  op = model.predict([ip])
  ans=op[0]
  if ans == 'Positive':
      st.success("Positive 😊")
  elif ans == 'Negative':
      st.error("Negative 😞")
  elif ans== 'Neutral':
      st.warning("Neutral 😐")
