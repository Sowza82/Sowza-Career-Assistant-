"""
============================================================
TESTE DO RETRIEVER
Sowza Career Assistant
============================================================

Este teste verifica se o banco vetorial pode ser
carregado corretamente e se o retriever retorna
os documentos mais relevantes para uma consulta.

Versão: 2.0
"""

from src.retriever import create_retriever


def test_create_retriever():
    """Verifica se o retriever é criado corretamente."""

    retriever = create_retriever()

    assert retriever is not None, "Falha ao criar o retriever."


def test_retriever_query():
    """Verifica se o retriever retorna documentos para uma consulta."""

    retriever = create_retriever()

    consulta = "Quem é Tatiane Souza?"
    resultados = retriever.invoke(consulta)

    assert len(resultados) > 0, "Nenhum documento foi recuperado."

    primeiro = resultados[0]

    assert hasattr(primeiro, "page_content")
    assert primeiro.page_content.strip() != ""

    assert hasattr(primeiro, "metadata")
    assert isinstance(primeiro.metadata, dict)


def test_retriever_metadata():
    """Verifica se os documentos recuperados possuem a origem."""

    retriever = create_retriever()

    resultados = retriever.invoke("Quem é Tatiane Souza?")

    for doc in resultados:
        assert "source" in doc.metadata, (
            "Documento recuperado sem metadado 'source'."
        )
