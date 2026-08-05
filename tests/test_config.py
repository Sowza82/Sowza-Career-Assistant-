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

print("=" * 60)
print("TESTE DAS CONFIGURAÇÕES")
print("=" * 60)

print(f"API carregada: {bool(GOOGLE_API_KEY)}")
print(f"Modelo LLM: {LLM_MODEL}")
print(f"Modelo Embedding: {EMBEDDING_MODEL}")
print(f"Chunk Size: {CHUNK_SIZE}")
print(f"Chunk Overlap: {CHUNK_OVERLAP}")
print(f"Top K: {TOP_K}")
print(f"Search Type: {SEARCH_TYPE}")
print(f"Temperature: {TEMPERATURE}")
print(f"Max Output Tokens: {MAX_OUTPUT_TOKENS}")