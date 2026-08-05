"""
============================================================
VECTOR STORE
Sowza Career Assistant
============================================================

Responsável pela criação e persistência do banco vetorial
utilizando ChromaDB.

Versão: 2.0
"""

import re
import time

from langchain_chroma import Chroma

from src.config import VECTOR_DB_DIR
from src.embeddings import get_embeddings


def create_vector_store(
    chunks,
    batch_size=20,
    wait_time=10,
    max_retries=5,
):
    """
    Cria o banco vetorial utilizando processamento em lotes.

    Args:
        chunks: Lista de documentos.
        batch_size: Quantidade de chunks por lote.
        wait_time: Tempo padrão entre lotes.
        max_retries: Número máximo de tentativas em caso de erro 429.
    """

    embeddings = get_embeddings()

    vector_store = Chroma(
        embedding_function=embeddings,
        persist_directory=str(VECTOR_DB_DIR),
    )

    total = len(chunks)

    print("=" * 60)
    print("CRIANDO BANCO VETORIAL")
    print("=" * 60)
    print(f"Total de chunks: {total}")
    print(f"Tamanho do lote: {batch_size}")
    print()

    lote = 1

    for inicio in range(0, total, batch_size):

        fim = min(inicio + batch_size, total)

        documentos = chunks[inicio:fim]

        tentativa = 1

        while tentativa <= max_retries:

            try:

                print(f"Processando lote {lote} ({inicio+1}-{fim})...")

                vector_store.add_documents(documentos)

                print("OK\n")

                break

            except Exception as erro:

                mensagem = str(erro)

                if "RESOURCE_EXHAUSTED" not in mensagem:
                    raise erro

                tempo = wait_time

                resultado = re.search(r"retry in (\d+)", mensagem)

                if resultado:
                    tempo = int(resultado.group(1)) + 2

                print(
                    f"Limite da API atingido."
                )

                print(
                    f"Aguardando {tempo} segundos..."
                )

                time.sleep(tempo)

                tentativa += 1

        else:
            raise Exception(
                f"Falha ao processar o lote {lote} após {max_retries} tentativas."
            )

        lote += 1

        if fim < total:
            print(f"Esperando {wait_time} segundos antes do próximo lote...\n")
            time.sleep(wait_time)

    print("=" * 60)
    print("BANCO VETORIAL CRIADO COM SUCESSO")
    print("=" * 60)

    return vector_store
