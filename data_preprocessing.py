import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from scipy.sparse import save_npz
import nltk # for text preprocessing
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
import re, ast

# Load data
df = pd.read_csv('patent_claims.csv')

# Basic text cleaning function
def clean_text(text):
    """
    Cleans the given text by removing numbering like '16.', '2. ', and non-alphabet characters.
    The text is then converted to lowercase.

    Parameters:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Remove numbering like '16.', '2. '
    text = re.sub(r'\b\d+\.\s*', '', text)
    
    # Remove non-alphabet characters and lower the text
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = text.lower()
    return text

def normalize_text(text):
    """
    Normalizes the input text by lemmatizing words not in the stop words set.

    Parameters:
        text (str): The text to be normalized.

    Returns:
        str: The normalized text as a single string, with words separated by whitespace.
    """
    words = text.split() # Split the text into individual words using whitespace (tokes)
    
    # Remove stopwords and lemmatize words
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Tokenization and normalization function
nltk.download('stopwords', quiet=True) # for stopwords
nltk.download('wordnet', quiet=True) # for lemmatization, exmaple: ran, running -> run

# Extend the stop word list with custom domain-specific terms
custom_stop_words = ['said', 'claim', 'wherein', 'comprise', 'include', 'method', 'apparatus', 'second', 'according']
stop_words = set(stopwords.words('english')).union(custom_stop_words)
lemmatizer = WordNetLemmatizer()

# Prepare data by processing each claim
all_claims = []
for index, row in df.iterrows():
    # Try to convert the claims from string to list
    try:
        claims = ast.literal_eval(row['Claims']) # safely evaluates an expression node or a string containing a Python literal
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

# Create a DataFrame with the processed claims
df_processed = pd.DataFrame(all_claims)

# Vectorization - convert text to numerical data
vectorizer = TfidfVectorizer(max_features=1000) # init a TfidfVectorizer object
tfidf_matrix = vectorizer.fit_transform(df_processed['Normalized Claim'])

# Save matrix to a npz file - suitable for efficiently storing large sparse matrices
matrix_file_path = 'tfidf_matrix.npz'
save_npz(matrix_file_path, tfidf_matrix)
print("TF-IDF matrix saved successfully to:", matrix_file_path)

# Save DataFrame to CSV
df_file_path = 'normalized_patent_claims.csv'
df_processed.to_csv(df_file_path, index=False)
print("DataFrame saved successfully to:", df_file_path)

print('Done data_preprocessing!')
