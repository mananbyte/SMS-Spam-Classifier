import nltk
import os
import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# Ensure required NLTK data is available in a writable local folder.
# Create a local `nltk_data` directory in the repo (or fall back to /tmp)
nl_dir = os.path.join(os.getcwd(), 'nltk_data')
try:
    os.makedirs(nl_dir, exist_ok=True)
except Exception:
    nl_dir = '/tmp/nltk_data'

# Prefer local nltk_data first
if nl_dir not in nltk.data.path:
    nltk.data.path.insert(0, nl_dir)

def _ensure_nltk(resource_path, pkg_name=None):
    try:
        nltk.data.find(resource_path)
    except LookupError:
        name = pkg_name if pkg_name else resource_path.split('/')[-1]
        nltk.download(name, download_dir=nl_dir, quiet=True)

_ensure_nltk('tokenizers/punkt', 'punkt')
_ensure_nltk('corpora/stopwords', 'stopwords')
_ensure_nltk('tokenizers/punkt_tab/english', 'punkt_tab')


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


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
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
