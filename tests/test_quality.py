from src.loader import load_documents
from src.splitter import split_documents


def test_no_empty_documents():
    """Verifica se existem documentos sem conteúdo."""

    documents = load_documents()

    empty_docs = [
        doc for doc in documents
        if not doc.page_content.strip()
    ]

    assert len(empty_docs) == 0, (
        f"Encontrados {len(empty_docs)} documentos vazios."
    )


def test_no_small_chunks():
    """Verifica se existem chunks menores que o limite definido."""

    documents = load_documents()
    chunks = split_documents(documents)

    small_chunks = [
        chunk for chunk in chunks
        if len(chunk.page_content) < 100
    ]

    assert len(small_chunks) == 0, (
        f"Encontrados {len(small_chunks)} chunks muito pequenos."
    )


def test_no_spacing_problems():
    """Verifica possíveis problemas de espaçamento no texto."""

    documents = load_documents()
    chunks = split_documents(documents)

    padroes_problematicos = [
        "soluçõesdigitais",
        "nodesenvolvimento",
        "comfoco",
        "tecnologia.A",
        "profissionalpor",
    ]

    problemas = []

    for chunk in chunks:
        for padrao in padroes_problematicos:
            if padrao in chunk.page_content:
                problemas.append(padrao)

    assert len(problemas) == 0, (
        f"Encontrados padrões problemáticos: {problemas}"
    )


def test_chunks_statistics():
    """Verifica se os chunks possuem tamanho válido."""

    documents = load_documents()
    chunks = split_documents(documents)

    tamanhos = [
        len(chunk.page_content)
        for chunk in chunks
    ]

    assert len(tamanhos) > 0
    assert min(tamanhos) > 0
    assert max(tamanhos) >= min(tamanhos)
