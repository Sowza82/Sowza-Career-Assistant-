from src.loader import load_documents
from src.splitter import split_documents


documents = load_documents()

chunks = split_documents(documents)


print("=" * 60)
print("TESTE SPLITTER")
print("=" * 60)

print(f"Documentos originais: {len(documents)}")
print(f"Chunks gerados: {len(chunks)}")


print("\nPrimeiro chunk:")
print("-" * 60)

print(chunks[0].page_content)
