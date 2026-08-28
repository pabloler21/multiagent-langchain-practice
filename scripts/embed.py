# DO NOT USE: from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small")

def embed_text(documents:list) -> list[float]:
    embed_documents = embeddings.embed_documents(documents)
    return embed_documents

if __name__ == "__main__":
    """from loader import load_documents_from_folder
    from splitter import split_documents_into_chunks
    
    # Load documents from the specified folder
    documents = load_documents_from_folder("data\\finance_docs")
    # Split documents into chunks
    chunks = split_documents_into_chunks(documents)

    # Embed each chunk and print the first 5 embeddings
    for i, chunk in enumerate(chunks[:5]):
        embedding_vector = embed_text(chunk["text"])
        print(f"Chunk {i} embedding: {embedding_vector[:5]}...")  # Print first 5 dimensions of the embedding"""