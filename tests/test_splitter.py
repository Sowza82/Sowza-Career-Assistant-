from src.loader import load_documents
from src.splitter import split_documents


def test_split_documents():
    """Verifica se o splitter gera chunks a partir dos documentos."""

    documents = load_documents()
    chunks = split_documents(documents)

    assert len(documents) > 0, "Nenhum documento foi carregado."
    assert len(chunks) > 0, "Nenhum chunk foi gerado."

    # O splitter deve gerar pelo menos a mesma quantidade de chunks
    # que documentos (normalmente gera bem mais).
    assert len(chunks) >= len(documents)


def test_chunk_content():
    """Verifica se o primeiro chunk possui conteúdo."""

    documents = load_documents()
    chunks = split_documents(documents)

    assert hasattr(chunks[0], "page_content")
    assert chunks[0].page_content.strip() != ""


def test_chunk_metadata():
    """Verifica se os chunks possuem metadados."""

    documents = load_documents()
    chunks = split_documents(documents)

    assert hasattr(chunks[0], "metadata")
    assert isinstance(chunks[0].metadata, dict)
