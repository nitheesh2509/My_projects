import pandas as pd
import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Download NLTK resources
nltk.download('stopwords')

# Load dataset
news_data = pd.read_csv('train.csv')
news_data.fillna(' ', inplace=True)
news_data['content'] = news_data['author'] + " " + news_data['title']

# Initialize Porter Stemmer and stopwords
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Preprocess text
def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)  # Remove non-alphabetic characters
    text = text.lower()  # Convert text to lowercase
    text = text.split()  # Tokenize text
    text = [ps.stem(word) for word in text if word not in stop_words]  # Stemming and remove stopwords
    text = ' '.join(text)  # Join tokens back into a string
    return text

# Apply preprocessing to dataset
news_data['content'] = news_data['content'].apply(preprocess_text)

# Split data into features and target
X = news_data['content'].values
Y = news_data['label'].values

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)

# Fit and transform the text data
X = vectorizer.fit_transform(X)

# Split data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Initialize Logistic Regression model
model = LogisticRegression()

# Fit the model
model.fit(X_train, Y_train)

# Save vectorizer and model
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'model.pkl')

# Load vectorizer and model
vectorizer = joblib.load('vectorizer.pkl')
model = joblib.load('model.pkl')

# Initialize Streamlit app
st.title("Fake News Detection")
input_text = st.text_input("Enter news article: ")

# Prediction function
def predict(input_text):
    input_data = [input_text]
    vectorized_input_data = vectorizer.transform(input_data)
    prediction = model.predict(vectorized_input_data)
    return prediction[0]

# Display prediction
if input_text:
    prediction = predict(input_text)
    if prediction == 1:
        st.write("This is Fake News")
    else:
        st.write("This is True News")
