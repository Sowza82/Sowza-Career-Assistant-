from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Divide documentos em partes menores para processamento RAG.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        length_function=len,
        separators=[
            "\n\n",
            "\n",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(documents)

    return chunks
