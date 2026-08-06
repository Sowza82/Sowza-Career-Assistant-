"""
============================================================
TESTES DOS UTILITÁRIOS
Sowza Career Assistant
============================================================

Testes das funções auxiliares.

Versão: 2.0
"""

from src.utils import (
    normalize_text,
    validate_question,
)


def test_normalize_text():
    """
    Verifica se espaços extras são removidos.
    """

    text = "  Tatiane     Souza   "

    assert normalize_text(text) == "Tatiane Souza"


def test_validate_question_valid():
    """
    Verifica pergunta válida.
    """

    assert validate_question(
        "Quem é Tatiane Souza?"
    )


def test_validate_question_empty():
    """
    Verifica pergunta vazia.
    """

    assert not validate_question("")


def test_validate_question_spaces():
    """
    Verifica pergunta contendo apenas espaços.
    """

    assert not validate_question("      ")
