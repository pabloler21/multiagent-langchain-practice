from langchain_docling.loader import DoclingLoader
from pathlib import Path


def load_documents_from_folder(folder_path: str) -> list[dict]:

    loader = DoclingLoader(file_path=folder_path, file_type="md", recursive=True)

    # Load all documents
    documents = loader.load()

    # For large datasets, lazily load documents
    for document in documents:
        print(document)