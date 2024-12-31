import streamlit as st
from textblob import TextBlob
st.sidebar.image("dilip.jpg")
st.sidebar.title("About Me")
st.sidebar.text(""" I am Dilip Prajapati
a Data science Student from
Ducat institute Noida
""")


st.sidebar.title("Contact Me")
st.sidebar.text(""" Name: Dilip Prajapati
Course :Data science & Machine learning
Mob : 8745024207
Email :dilip.prajapati.ichak@gmail.com
""")


st.title("Sentiment Analysis Project")

text=st.text_input("**enter text**")
btn=st.button("Predict")

if btn:
    blob=TextBlob(text)
    sent=blob.sentiment[0]
    if sent<0:
        st.error("Negative Sentiment")
        st.image("Sentiment_images/neg_senti.jpg")
    elif sent>0:
        st.success("Positive Sentiment")
        st.image("Sentiment_images/pos_senti.jpg")
    else:
        st.warning("Neutral Sentiment")
        st.image("Sentiment_images/neutral_senti.jpg")
