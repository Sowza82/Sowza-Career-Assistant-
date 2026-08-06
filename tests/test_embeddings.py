"""
============================================================
TESTE DOS EMBEDDINGS
Sowza Career Assistant
============================================================
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import EMBEDDING_MODEL, GOOGLE_API_KEY


def test_google_api_key():
    """Verifica se a chave da API está configurada."""
    assert GOOGLE_API_KEY, "A GOOGLE_API_KEY não foi carregada."


def test_embedding_model():
    """Verifica se o modelo de embeddings foi configurado."""
    assert EMBEDDING_MODEL, "O modelo de embeddings não foi definido."


def test_generate_embedding():
    """Verifica se é possível gerar um embedding."""

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY,
    )

    texto = "Olá, mundo!"
    vetor = embeddings.embed_query(texto)

    assert isinstance(vetor, list)
    assert len(vetor) > 0, "O vetor de embedding está vazio."

    # Todos os elementos devem ser numéricos
    assert all(isinstance(valor, (float, int)) for valor in vetor)
