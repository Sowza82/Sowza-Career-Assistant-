"""
============================================================
UTILITÁRIOS
Sowza Career Assistant
============================================================

Funções auxiliares utilizadas pelo projeto.

Versão: 2.0
"""

import time
from functools import wraps


def normalize_text(text: str) -> str:
    """
    Remove espaços excedentes de um texto.

    Parameters
    ----------
    text : str
        Texto a ser normalizado.

    Returns
    -------
    str
        Texto normalizado.
    """

    return " ".join(text.split())


def validate_question(question: str) -> bool:
    """
    Valida uma pergunta do usuário.

    Parameters
    ----------
    question : str

    Returns
    -------
    bool
    """

    return bool(question and question.strip())


def execution_time(func):
    """
    Decorador para medir o tempo de execução de uma função.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"{func.__name__} executado em {end - start:.3f}s")

        return result

    return wrapper
