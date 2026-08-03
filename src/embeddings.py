"""
============================================================
EMBEDDINGS
Sowza Career Assistant
============================================================

Centraliza a configuração e a criação do modelo
de embeddings utilizado pelo projeto.

Versão: 2.0
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import (
    GOOGLE_API_KEY,
    EMBEDDING_MODEL,
)


def get_embeddings():
    """
    Retorna uma instância do modelo de embeddings
    configurado para o projeto.
    """

    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY,
    )
