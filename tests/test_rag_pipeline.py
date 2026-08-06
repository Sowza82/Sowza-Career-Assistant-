"""
============================================================
TESTE DO RAG PIPELINE
Sowza Career Assistant
============================================================

Testes do pipeline principal do sistema RAG.

Versão: 2.0
"""

from src.rag_pipeline import ask


def test_pipeline_returns_string():
    """Verifica se o pipeline retorna uma string."""

    response = ask("Quem é Tatiane Souza?")

    assert isinstance(response, str)


def test_pipeline_not_empty():
    """Verifica se a resposta não está vazia."""

    response = ask("Quem é Tatiane Souza?")

    assert len(response.strip()) > 0


def test_pipeline_contains_name():
    """Verifica se a resposta contém o nome Tatiane Souza."""

    response = ask("Quem é Tatiane Souza?")

    assert "Tatiane Souza" in response


def test_pipeline_professional_context():
    """Verifica se a resposta está relacionada ao contexto profissional."""

    response = ask("Quem é Tatiane Souza?")

    keywords = [
        "SowzaTech",
        "desenvolvimento",
        "Front-End",
        "tecnologia",
        "projetos",
    ]

    assert any(keyword in response for keyword in keywords)
