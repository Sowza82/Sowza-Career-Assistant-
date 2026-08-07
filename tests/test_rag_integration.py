"""
Testes de integração do pipeline RAG.

Valida o fluxo completo:

Pergunta do usuário
        ↓
Retriever
        ↓
Contexto recuperado
        ↓
Prompt
        ↓
LLM Gemini
        ↓
Resposta final

Versão: 2.0
"""

from src.rag_pipeline import ask


def test_rag_full_pipeline():
    """
    Verifica se o pipeline RAG consegue processar
    uma pergunta e retornar uma resposta válida.
    """

    question = "Quem é Tatiane Souza?"

    response = ask(question)

    assert response is not None
    assert isinstance(response, str)
    assert len(response.strip()) > 0


def test_rag_response_identity():
    """
    Verifica se a resposta mantém a identidade
    profissional da Tatiane Souza.
    """

    response = ask(
        "Quem é Tatiane Souza?"
    )

    keywords = [
        "Tatiane Souza",
        "SowzaTech",
        "tecnologia",
        "Front-End",
    ]

    assert any(
        keyword.lower() in response.lower()
        for keyword in keywords
    )


def test_rag_response_project_context():
    """
    Verifica se o pipeline consegue recuperar
    informações relacionadas às tecnologias da
    trajetória profissional.
    """

    response = ask(
        "Quais tecnologias fazem parte da trajetória profissional?"
    )

    keywords = [
        "Python",
        "JavaScript",
        "React",
        "LangChain",
        "IA",
    ]

    assert any(
        keyword.lower() in response.lower()
        for keyword in keywords
    )
