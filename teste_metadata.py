from src.loader import load_documents
from src.splitter import split_documents


print("=" * 60)
print("TESTE METADADOS DOS CHUNKS")
print("=" * 60)


documents = load_documents()

print()
print(f"Documentos carregados: {len(documents)}")


chunks = split_documents(documents)

print(f"Chunks gerados: {len(chunks)}")


print()
print("Primeiros 5 chunks")
print("=" * 60)


for i, chunk in enumerate(chunks[:5], start=1):

    print()
    print(f"CHUNK {i}")
    print("-" * 60)

    print("Metadados:")
    print(chunk.metadata)

    print()

    print("Tamanho:")
    print(f"{len(chunk.page_content)} caracteres")

    print()

    print("Conteúdo inicial:")
    print(chunk.page_content[:300])

    print()
