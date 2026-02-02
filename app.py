import nltk
import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    # Lower Case
    text = text.lower()

    # Tokenization
    text = nltk.word_tokenize(text)

    # Removing Special Characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    # Removing Stopwords and Punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    # Stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl.', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Spam Classifier')
input_sms = st.text_area("Enter the message to classify")

if st.button('Predict'):
    #Prepocessing of Data
    transformed_sms = transform_text(input_sms)
    # Vectorization
    vector_input = tfidf.transform([transformed_sms])
    #prediction
    result = model.predict(vector_input)
    # Displaying
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
