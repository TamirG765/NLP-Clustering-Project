from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def perform_clustering(embeddings, n_clusters):
    """
    Perform k-means clustering on the given embeddings.

    Parameters:
    - embeddings: The data points to cluster.
    - n_clusters: The number of clusters to form.

    Returns:
    - labels: Array of cluster labels for each data point.
    - counts: Number of points in each cluster.
    """
    
    # Perform k-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(embeddings)
    
    # Get cluster labels for each point
    labels = kmeans.labels_
    
    # Count the number of points in each cluster
    counts = np.bincount(labels)
    return labels, counts

def get_top_words(texts, labels):
    """
    Get the top words from each cluster in the given texts and labels.

    Parameters:
    - texts (list): A list of normalized claims.
    - labels (list): A list of cluster labels corresponding to the claims.

    Returns:
    - top_words_from_clusters (dict): A dictionary where the keys are cluster labels and the values are the top words from each cluster.
    """
    # Convert lists to DataFrame
    df = pd.DataFrame({'Normalized Claim': texts, 'Cluster Label': labels})
    
    # Apply the existing logic
    grouped = df.groupby('Cluster Label')['Normalized Claim'].apply(list)
    top_words_from_clusters = {}
    
    for label, claims in grouped.items():
        top_word = apply_lda_to_cluster(claims)
        top_words_from_clusters[label] = top_word

    return top_words_from_clusters

# Function to apply LDA to each cluster, remains the same
def apply_lda_to_cluster(texts):
    """
    Apply Latent Dirichlet Allocation (LDA) to the given texts to find the top word in the cluster.

    Parameters:
    - texts (list): A list of texts to apply LDA on.

    Returns:
    - top_word (str): The top word identified by LDA in the cluster.
    """
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer(stop_words='english', token_pattern=r'\b[a-zA-Z]{2,}\b')
    
    # Fit the model
    tf = vectorizer.fit_transform(texts)
    
    # Initialize the LDA model with 1 component (topic)
    lda = LatentDirichletAllocation(n_components=1, random_state=42)
    
    # Fit the LDA model to the document-term matrix
    lda.fit(tf)
    
    # Retrieve the feature names (words) from the vectorizer
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the topic's array of word importance, which only has one topic in this case
    topic = lda.components_[0]
    
    # Find the index of the word with the highest weight in the topic
    top_word_index = topic.argsort()[-1]
    
    # Retrieve the actual word corresponding to the highest weight
    top_word = feature_names[top_word_index]
    
    return top_word
