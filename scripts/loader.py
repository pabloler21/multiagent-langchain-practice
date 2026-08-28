from pathlib import Path
from langchain_docling.loader import DoclingLoader

def load_documents_from_folder(folder_path: str) -> list:
    # 1. Buscamos todos los archivos .md en la carpeta
    file_paths = []
    for p in Path(folder_path).glob("*.md"):
        file_paths.append(str(p))
    
    # 2. Le pasamos la lista de archivos a DoclingLoader
    loader = DoclingLoader(file_path=file_paths)
    return loader.load()


if __name__ == "__main__":
    # Example usage:
    docs = load_documents_from_folder("data\\finance_docs")
    print(docs[0].page_content)  # Print the content of the first document