import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import save_npz
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Load data
df = pd.read_csv('patent_claims.csv')

# Basic text cleaning
def clean_text(text):
    # Remove numbering like '16.', '2. '
    text = re.sub(r'\b\d+\s*', '', text)
    
    # Remove non-alphabet characters and lower the text
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = text.lower()
    return text

# Apply text cleaning
df['cleaned_claims'] = df['Claims'].apply(clean_text)

# Tokenization and normalization
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def normalize_text(text):
    words = text.split()
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(filtered_words)

df['normalized_claims'] = df['cleaned_claims'].apply(normalize_text)

# Vectorization
vectorizer = TfidfVectorizer(max_features=1000)
tfidf_matrix = vectorizer.fit_transform(df['normalized_claims'])

# Save matrix to a file for later use
matrix_file_path = 'tfidf_matrix.npz'
save_npz(matrix_file_path, tfidf_matrix)
print("TF-IDF matrix saved successfully to:", matrix_file_path)

# Convert matrix to DataFrame and show example
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Save DataFrame to CSV
df_file_path = 'processed_patent_claims.csv'
df.to_csv(df_file_path, index=False)
print("DataFrame saved successfully to:", df_file_path)
