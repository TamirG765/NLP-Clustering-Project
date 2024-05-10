import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import save_npz
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re, ast

# Load data
df = pd.read_csv('patent_claims.csv')

# Basic text cleaning function
def clean_text(text):
    # Remove numbering like '16.', '2. '
    text = re.sub(r'\b\d+\.\s*', '', text)
    
    # Remove non-alphabet characters and lower the text
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = text.lower()
    return text

# Tokenization and normalization function
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def normalize_text(text):
    words = text.split()
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Prepare data by processing each claim
all_claims = []
for index, row in df.iterrows():
    # Assume the claims are stored as a string representation of a list; safely convert back to list
    try:
        claims = ast.literal_eval(row['Claims'])
    except ValueError:
        # Fallback if the conversion fails
        claims = [row['Claims']]
    
    for claim in claims:
        cleaned_claim = clean_text(claim)
        normalized_claim = normalize_text(cleaned_claim)
        all_claims.append({
            'Patent URL': row['Patent URL'],
            'Normalized Claim': normalized_claim
        })

# Create a DataFrame with the expanded and processed claims
df_expanded = pd.DataFrame(all_claims)

# Vectorization
vectorizer = TfidfVectorizer(max_features=1000)
tfidf_matrix = vectorizer.fit_transform(df_expanded['Normalized Claim'])

# Save matrix to a file for later use
matrix_file_path = 'tfidf_matrix.npz'
save_npz(matrix_file_path, tfidf_matrix)
print("TF-IDF matrix saved successfully to:", matrix_file_path)

# Save DataFrame to CSV
df_file_path = 'processed_patent_claims.csv'
df_expanded.to_csv(df_file_path, index=False)
print("DataFrame saved successfully to:", df_file_path)

print('Done data_preprocessing!')
