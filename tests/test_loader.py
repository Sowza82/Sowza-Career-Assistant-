from src.loader import (
    load_documents,
    list_documents,
    total_documents,
)


def test_list_documents():
    """Verifica se existem documentos na base de conhecimento."""
    arquivos = list_documents()

    assert isinstance(arquivos, list)
    assert len(arquivos) > 0, "Nenhum documento encontrado."


def test_total_documents():
    """Verifica se a quantidade de documentos está correta."""
    arquivos = list_documents()

    assert total_documents() == len(arquivos)


def test_load_documents():
    """Verifica se os documentos são carregados corretamente."""
    documents = load_documents()

    assert len(documents) > 0, "Nenhum documento foi carregado."

    # Verifica se o primeiro documento possui conteúdo
    assert hasattr(documents[0], "page_content")
    assert len(documents[0].page_content.strip()) > 0
