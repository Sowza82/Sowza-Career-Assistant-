"""
============================================================
RETRIEVER
Sowza Career Assistant
============================================================

Responsável por carregar o banco vetorial e criar
o Retriever utilizado pelo pipeline RAG.

Versão: 2.0
"""

from langchain_chroma import Chroma

from src.config import (
    VECTOR_DB_DIR,
    TOP_K,
    SEARCH_TYPE,
)
from src.embeddings import get_embeddings


def create_retriever():
    """
    Carrega o banco vetorial existente e cria
    um retriever para buscas semânticas.
    """

    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embeddings,
    )

    retriever = vector_store.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={
            "k": TOP_K
        },
    )

    return retriever
