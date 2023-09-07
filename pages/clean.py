import re
import string
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
nltk.download('stopwords')

def pipline_cleaning_step(text):
    tokens = re.findall(r'\b\w+\b', text)
 
    tokens = [token.lower() for token in tokens]
 
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
 
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Split text into words
    tokens = text.split()

    # Join the tokens back into a clean text
    clean_text = ' '.join(tokens)


    return clean_text