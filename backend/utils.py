import os
import fitz  # PyMuPDF for PDF processing

def load_documents(docs_folder: str):
    """
    Loads documents from the provided folder. If a PDF is detected, extracts text from it.
    """
    documents = []
    for filename in os.listdir(docs_folder):
        file_path = os.path.join(docs_folder, filename)
        
        if filename.endswith('.pdf'):
            # Extract text from PDF
            with fitz.open(file_path) as pdf:
                pdf_text = ""
                for page in pdf:
                    pdf_text += page.get_text()
                documents.append(pdf_text)
        elif filename.endswith('.txt'):
            # Load plain text files (if any)
            with open(file_path, 'r', encoding='utf-8') as f:
                documents.append(f.read())
        else:
            print(f"Unsupported file format: {filename}")
    
    return documents

def store_embeddings(embeddings, embeddings_folder: str, filename: str):
    """
    Save embeddings or FAISS index to disk.
    """
    import pickle
    os.makedirs(embeddings_folder, exist_ok=True)
    with open(os.path.join(embeddings_folder, filename), 'wb') as f:
        pickle.dump(embeddings, f)
