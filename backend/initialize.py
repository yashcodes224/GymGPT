from pipeline import add_documents_to_faiss

if __name__ == "__main__":
    docs_folder = r"C:\Users\ASUS\OneDrive\Desktop\GymGPT\backend\docs"
    embeddings_folder = r"C:\Users\ASUS\OneDrive\Desktop\GymGPT\backend\embeddings"
    print("Initializing FAISS index and storing embeddings...")
    add_documents_to_faiss(docs_folder, embeddings_folder)
    print("Initialization complete!")
