from src.loader import load_documents
from src.splitter import split_documents


def test_chunks_have_metadata():
    """Verifica se todos os chunks possuem metadados."""

    documents = load_documents()
    chunks = split_documents(documents)

    assert len(chunks) > 0, "Nenhum chunk foi gerado."

    for chunk in chunks:
        assert hasattr(chunk, "metadata")
        assert isinstance(chunk.metadata, dict)


def test_chunks_have_content():
    """Verifica se todos os chunks possuem conteúdo."""

    documents = load_documents()
    chunks = split_documents(documents)

    for chunk in chunks:
        assert chunk.page_content.strip() != ""
        assert len(chunk.page_content) > 0


def test_chunks_have_source_metadata():
    """Verifica se os chunks possuem o metadado 'source'."""

    documents = load_documents()
    chunks = split_documents(documents)

    for chunk in chunks:
        assert "source" in chunk.metadata, (
            "Chunk sem metadado 'source'."
        )
