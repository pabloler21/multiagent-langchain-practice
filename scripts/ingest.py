from langchain_chroma import Chroma
from embed import embeddings
from loader import load_documents_from_folder
from splitter import split_documents_into_chunks
from langchain_community.vectorstores.utils import filter_complex_metadata

# 1. Cargar documentos
raw_docs = load_documents_from_folder("data/finance_docs")

# 2. Dividir en chunks (objetos Document)
chunks = split_documents_into_chunks(raw_docs)
# Filtrar metadatos complejos
chunks = filter_complex_metadata(chunks)
print(f"Indexando {len(chunks)} chunks en ChromaDB...")

# 3. Guardar en Chroma
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="finance_collection",
    persist_directory="./chroma_db/finance",
)

# 4. Probar que busca bien (Retriever)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
test_query = "¿Cuál es el tope de gastos de comida?"
results = retriever.invoke(test_query)

print("\n--- Prueba de búsqueda ---")
for doc in results:
    print(f"- {doc.page_content[:100]}...")