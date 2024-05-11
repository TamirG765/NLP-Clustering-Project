import pandas as pd

def read_preprocess_csv(filepath):
    
    # Load the CSV file
    df = pd.read_csv(filepath)
    
    # Attach texts to column 'Normalized Claim'
    texts = df['Normalized Claim'].tolist()
    
    return texts