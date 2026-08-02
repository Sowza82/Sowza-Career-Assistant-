"""
============================================================
CARREGAMENTO DA BASE DE CONHECIMENTO
Sowza Career Assistant
============================================================

Responsável por localizar e carregar todos os documentos
Markdown da base de conhecimento.

Versão: 2.0
"""

from pathlib import Path

from langchain_community.document_loaders import TextLoader

from src.config import RAW_DATA_DIR


def load_documents():
    """
    Carrega todos os documentos .md da base de conhecimento.

    Returns
    -------
    list
        Lista de objetos Document.
    """

    documents = []

    markdown_files = sorted(RAW_DATA_DIR.glob("*.md"))

    if not markdown_files:
        raise FileNotFoundError(
            f"Nenhum arquivo Markdown encontrado em:\n{RAW_DATA_DIR}"
        )

    for file in markdown_files:

        loader = TextLoader(
            str(file),
            encoding="utf-8"
        )

        documents.extend(loader.load())

    return documents


def list_documents():
    """
    Retorna apenas os nomes dos documentos encontrados.
    """

    return sorted(
        file.name
        for file in RAW_DATA_DIR.glob("*.md")
    )


def total_documents():
    """
    Retorna a quantidade de documentos encontrados.
    """

    return len(list_documents())
