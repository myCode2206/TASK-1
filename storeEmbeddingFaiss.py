import faiss
import numpy as np

def store_embeddings_faiss(embedding):
    # Initialize FAISS index
    dimension = embedding.shape[0]  # Length of embedding vector
    index = faiss.IndexFlatL2(dimension)  # Using L2 distance for similarity search
    
    # Convert embedding to float32
    embedding = np.array([embedding], dtype='float32')  # FAISS expects float32
    index.add(embedding)  # Add the embedding to the index

    # Save the index to a file (optional)
    faiss.write_index(index, 'faiss_index.bin')
    print("Embeddings stored in FAISS.")
