from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def perform_clustering(embeddings, n_clusters):
    
    # Perform k-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(embeddings)
    
    # Get cluster labels for each point
    labels = kmeans.labels_
    
    # Count the number of points in each cluster
    counts = np.bincount(labels)
    return labels, counts

def get_top_words(texts, labels):
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
    vectorizer = CountVectorizer(stop_words='english', token_pattern=r'\b[a-zA-Z]{2,}\b')
    tf = vectorizer.fit_transform(texts)
    lda = LatentDirichletAllocation(n_components=1, random_state=42)
    lda.fit(tf)
    feature_names = vectorizer.get_feature_names_out()
    topic = lda.components_[0]
    top_word_index = topic.argsort()[-1]
    top_word = feature_names[top_word_index]
    return top_word
