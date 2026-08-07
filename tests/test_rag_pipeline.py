"""
Testes do pipeline principal do sistema RAG.

Versão: 2.0
"""

import pytest

from src.rag_pipeline import ask


@pytest.fixture(scope="module")
def rag_response():
    """
    Executa o pipeline uma vez e reutiliza a resposta nos testes.
    """
    return ask("Quem é Tatiane Souza?")


def test_pipeline_returns_string(rag_response):
    """Verifica se o pipeline retorna uma string."""

    assert isinstance(rag_response, str)


def test_pipeline_not_empty(rag_response):
    """Verifica se a resposta não está vazia."""

    assert len(rag_response.strip()) > 0


def test_pipeline_contains_name(rag_response):
    """Verifica se a resposta contém o nome Tatiane Souza."""

    assert "Tatiane Souza" in rag_response


def test_pipeline_professional_context(rag_response):
    """Verifica se a resposta está relacionada ao contexto profissional."""

    keywords = [
        "SowzaTech",
        "desenvolvimento",
        "Front-End",
        "tecnologia",
        "projetos",
    ]

    assert any(keyword in rag_response for keyword in keywords)
