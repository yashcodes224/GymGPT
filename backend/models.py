from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the Sentence Transformer model for embeddings
embedding_model_name = 'nomic-ai/nomic-embed-text-v1-ablated'
embed_model = SentenceTransformer(embedding_model_name, trust_remote_code=True)

# Load GPT-2 model for generating responses
llm_model_name = 'gpt2'
llm_tokenizer = AutoTokenizer.from_pretrained(llm_model_name)
llm_model = AutoModelForCausalLM.from_pretrained(llm_model_name)
