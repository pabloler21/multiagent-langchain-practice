from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path



from pathlib import Path
from langchain_core.documents import Document

def load_documents_from_folder(folder_path: str) -> list[Document]:
    """Carga todos los archivos .md de una carpeta y los convierte en Documents de LangChain."""
    path = Path(folder_path)
    documents = []
    
    # Busca todos los archivos .md en la carpeta
    for file_path in path.glob("*.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Creamos el Document con su contenido y su metadata (nombre del archivo)
        doc = Document(
            page_content=content,
            metadata={"source": file_path.name, "domain": path.name}
        )
        documents.append(doc)
        
    return documents

# Ejemplo de uso:
# hr_raw_docs = load_documents_from_folder("data/hr_docs")
# print(f"Cargados {len(hr_raw_docs)} documentos de HR")