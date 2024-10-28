import numpy as np
import faiss

def query_embeddings_faiss(query_embedding, k=5):
    # Load the existing index
    index = faiss.read_index('faiss_index.bin')
    
    # Convert query embedding to float32
    query_embedding = np.array([query_embedding], dtype='float32')

    # Perform the search
    distances, indices = index.search(query_embedding, k)  # k nearest neighbors
    return distances, indices