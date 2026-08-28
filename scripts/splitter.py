from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents_into_chunks(documents: list) -> list:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    """text_chunks = split_documents_into_chunks(load_documents_from_folder("data\\finance_docs"))
    print(f"Total chunks created: {len(text_chunks)}")
    for i in range(len(text_chunks[:3])):  # Print first 100 characters of each chunk
        print(f"example chunk {text_chunks[i]}")"""