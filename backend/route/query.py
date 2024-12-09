from backend.pipeline import add_documents_to_faiss, generate_answer, search_documents

def get_answer(query):
    # Ensure documents (from the PDF) are added to the FAISS index
    add_documents_to_faiss('backend/docs', 'backend/embeddings')
    
    # Search for relevant documents from the FAISS index
    indices, _ = search_documents(query, 'backend/embeddings/faiss.index', k=3)
    
    # Retrieve the actual document text using indices
    context = []
    for idx in indices[0]:  # Assuming indices[0] gives the list of top 3 document indices
        # Since we're working with a single document, all indices will point to different sections of the PDF
        # For simplicity, let's retrieve all the text chunks (you can adjust to refine this)
        with open(f"backend/docs/gym.pdf", "rb") as doc_file:
            # We could split and load specific sections of the PDF using the `idx`, but for now, 
            # let's just load the whole document and use it as context
            context.append(doc_file.read().decode('utf-8'))  # Assuming UTF-8 encoding
    
    # Generate and return the answer using the context and query
    answer = generate_answer(context, query)
    return answer
