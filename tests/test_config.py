from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,
    SEARCH_TYPE,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
)


def test_google_api_key():
    """Verifica se a chave da API foi carregada."""
    assert GOOGLE_API_KEY, "A GOOGLE_API_KEY não foi carregada."


def test_models():
    """Verifica se os modelos foram configurados."""
    assert LLM_MODEL, "O modelo LLM não foi definido."
    assert EMBEDDING_MODEL, "O modelo de embeddings não foi definido."


def test_chunk_configuration():
    """Verifica a configuração dos chunks."""
    assert CHUNK_SIZE > 0, "CHUNK_SIZE deve ser maior que zero."
    assert CHUNK_OVERLAP >= 0, "CHUNK_OVERLAP não pode ser negativo."
    assert CHUNK_OVERLAP < CHUNK_SIZE, (
        "CHUNK_OVERLAP deve ser menor que CHUNK_SIZE."
    )


def test_retriever_configuration():
    """Verifica as configurações do retriever."""
    assert TOP_K > 0, "TOP_K deve ser maior que zero."
    assert SEARCH_TYPE, "SEARCH_TYPE não foi definido."


def test_generation_configuration():
    """Verifica as configurações do modelo de geração."""
    assert TEMPERATURE >= 0, "TEMPERATURE não pode ser negativa."
    assert MAX_OUTPUT_TOKENS > 0, (
        "MAX_OUTPUT_TOKENS deve ser maior que zero."
    )
