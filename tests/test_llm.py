"""
============================================================
TESTE DO LLM
Sowza Career Assistant
============================================================

Valida a criação do modelo Gemini utilizado
para geração das respostas.

Versão: 2.0
"""

from src.llm import get_llm


def test_create_llm():
    """
    Verifica se o modelo LLM é criado corretamente.
    """

    llm = get_llm()

    assert llm is not None
