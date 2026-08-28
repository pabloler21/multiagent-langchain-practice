from langchain_chroma import Chroma
from embed import embeddings
from loader import load_documents_from_folder
from splitter import split_documents_into_chunks
from langchain_community.vectorstores.utils import filter_complex_metadata

# 1. Cargar documentos de los 3 dominios
raw_docs_finance = load_documents_from_folder("data/finance_docs")
raw_docs_hr = load_documents_from_folder("data/hr_docs")
raw_docs_tech = load_documents_from_folder("data/tech_docs")  # <-- Corregido: tech_docs

# 2. Dividir en chunks
chunks_finance = split_documents_into_chunks(raw_docs_finance)
chunks_hr = split_documents_into_chunks(raw_docs_hr)
chunks_tech = split_documents_into_chunks(raw_docs_tech)

# 3. Filtrar metadatos complejos
chunks_finance = filter_complex_metadata(chunks_finance)
chunks_hr = filter_complex_metadata(chunks_hr)
chunks_tech = filter_complex_metadata(chunks_tech)

print(f"Indexando {len(chunks_finance)} chunks de finanzas en ChromaDB...")
print(f"Indexando {len(chunks_hr)} chunks de recursos humanos en ChromaDB...")
print(f"Indexando {len(chunks_tech)} chunks de tecnología en ChromaDB...")


def load_vector_stores(embeddings, chunks, collection_name, persist_directory):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory=persist_directory,
    )
    print(f"Vector store '{collection_name}' guardado en {persist_directory}.")
    return vector_store


def retrieve_documents(vector_store, query, k=2):
    # Acceso al nombre de la colección con _collection.name
    print(f"Buscando en la colección '{vector_store._collection.name}' para: '{query}'")
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    results = retriever.invoke(query)
    return results  # <-- Retorna la lista de Documents, no un string


if __name__ == "__main__":
    # Guardar / Cargar las 3 colecciones
    vs_finance = load_vector_stores(embeddings, chunks_finance, "finance_docs", "./chroma_db/finance")
    vs_hr = load_vector_stores(embeddings, chunks_hr, "hr_docs", "./chroma_db/hr")
    vs_tech = load_vector_stores(embeddings, chunks_tech, "tech_docs", "./chroma_db/tech")

    # Prueba de búsqueda
    print("\n--- Prueba de búsqueda ---")
    docs = retrieve_documents(vs_finance, "¿Cuál es el límite de gastos de comida?", k=2)
    for doc in docs:
        print(f"- {doc.page_content[:100]}...")