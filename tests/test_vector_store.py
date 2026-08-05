from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store

print("=" * 60)
print("TESTE DO VECTOR STORE")
print("=" * 60)

documents = load_documents()

chunks = split_documents(documents)

print(f"Documentos: {len(documents)}")
print(f"Chunks: {len(chunks)}")
print()

vector_store = create_vector_store(
    chunks=chunks,
    batch_size=20,
    wait_time=10,
)

print()
print("=" * 60)
print("TESTE FINALIZADO COM SUCESSO")
print("=" * 60)
