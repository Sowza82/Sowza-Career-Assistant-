"""
============================================================
LLM
Sowza Career Assistant
============================================================

Responsável pela configuração do modelo de linguagem
utilizado pelo assistente.

Versão: 2.0
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
)


def get_llm():
    """
    Retorna o modelo Gemini configurado.
    """

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUT_TOKENS,
    )

    return llm
