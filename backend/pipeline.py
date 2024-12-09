import faiss
import numpy as np
from backend.models import embed_model, llm_model, llm_tokenizer
from backend.utils import load_documents, store_embeddings

# Setup FAISS index
embedding_dimension = 768  # Adjust based on the embedding model's output
index = faiss.IndexFlatL2(embedding_dimension)

# Embed documents and store them in FAISS
def add_documents_to_faiss(docs_folder: str, embeddings_folder: str):
    """
    Load documents from the specified folder, embed them, and add to the FAISS index.
    """
    documents = load_documents(docs_folder)
    embeddings = embed_model.encode(documents, convert_to_numpy=True)
    faiss.normalize_L2(embeddings)
    index.add(embeddings)
    store_embeddings(embeddings, embeddings_folder, 'index.pkl')

# Generate an answer using the GPT-2 model
def generate_answer(context, query):
    """
    Generate a response to the query based on the context using GPT-2.
    """
    input_text = f"Answer the following question based on the context: {query}\n\nContext:\n" + "\n".join(context)
    inputs = llm_tokenizer(input_text, return_tensors="pt", truncation=True, max_length=1024)
    outputs = llm_model.generate(**inputs, max_length=500, num_return_sequences=1)
    answer = llm_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.strip()

# Search the FAISS index for relevant documents
def search_documents(query, k=3):
    """
    Search the FAISS index for the top-k relevant documents for a given query.
    """
    query_embedding = embed_model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(query_embedding)
    distances, indices = index.search(query_embedding, k)
    # Access the documents corresponding to the retrieved indices
    return [documents[i] for i in indices[0]]
