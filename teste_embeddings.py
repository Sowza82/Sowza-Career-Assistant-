"""
============================================================
TESTE DOS EMBEDDINGS
Sowza Career Assistant
============================================================
"""

from src.config import GOOGLE_API_KEY, EMBEDDING_MODEL
from langchain_google_genai import GoogleGenerativeAIEmbeddings


print("=" * 60)
print("TESTE DOS EMBEDDINGS")
print("=" * 60)

# Verifica a API Key
if GOOGLE_API_KEY:
    print("API Key carregada: OK")
else:
    print("API Key NÃO encontrada!")
    exit()

print(f"Modelo: {EMBEDDING_MODEL}")

try:
    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )

    texto = "Olá, mundo!"

    vetor = embeddings.embed_query(texto)

    print("\nEmbedding gerado com sucesso!")
    print(f"Dimensão do vetor: {len(vetor)}")

    print("\nPrimeiros 10 valores:")
    print(vetor[:10])

except Exception as e:
    print("\nErro ao gerar embedding:")
    print(e)
