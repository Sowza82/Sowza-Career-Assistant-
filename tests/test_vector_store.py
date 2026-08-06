from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store


def test_create_vector_store():
    """Verifica se o Vector Store é criado corretamente."""

    documents = load_documents()
    assert len(documents) > 0, "Nenhum documento carregado."

    chunks = split_documents(documents)
    assert len(chunks) > 0, "Nenhum chunk foi gerado."

    vector_store = create_vector_store(
        chunks=chunks,
        batch_size=20,
        wait_time=10,
    )

    assert vector_store is not None, "Falha ao criar o Vector Store."
