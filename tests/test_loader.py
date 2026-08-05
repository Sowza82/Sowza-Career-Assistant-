from src.loader import (
    load_documents,
    list_documents,
    total_documents
)

print("=" * 60)
print("DOCUMENTOS ENCONTRADOS")
print("=" * 60)

arquivos = list_documents()

for i, arquivo in enumerate(arquivos, start=1):
    print(f"{i:02d}. {arquivo}")

print()

print("Total:", total_documents())

print()

documents = load_documents()

print("Documentos carregados:", len(documents))
