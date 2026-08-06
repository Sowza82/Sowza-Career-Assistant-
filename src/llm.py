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
    Retorna uma instância do modelo Gemini configurado.

    Para modelos que utilizam configurações de amostragem fixas
    (como o gemini-3.6-flash), o parâmetro temperature não é
    enviado para evitar warnings da API.
    """

    llm_config = {
        "model": LLM_MODEL,
        "google_api_key": GOOGLE_API_KEY,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
    }

    # Apenas adiciona temperature para modelos que suportam
    # essa configuração.
    if LLM_MODEL != "gemini-3.6-flash":
        llm_config["temperature"] = TEMPERATURE

    return ChatGoogleGenerativeAI(**llm_config)
