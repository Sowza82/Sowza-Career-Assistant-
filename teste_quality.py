from src.loader import load_documents
from src.splitter import split_documents


print("=" * 60)
print("TESTE DE QUALIDADE DA BASE")
print("=" * 60)


# Carregar documentos
documents = load_documents()

print(f"\nDocumentos analisados: {len(documents)}")


# Verificar documentos vazios
print("\n1. DOCUMENTOS VAZIOS")
print("-" * 60)

empty_docs = []

for doc in documents:
    if not doc.page_content.strip():
        empty_docs.append(doc.metadata)

if empty_docs:
    print("Documentos vazios encontrados:")
    for item in empty_docs:
        print(item)
else:
    print("Nenhum documento vazio encontrado.")


# Criar chunks
chunks = split_documents(documents)

print("\nChunks analisados:", len(chunks))


# Verificar chunks pequenos
print("\n2. CHUNKS MUITO PEQUENOS")
print("-" * 60)

small_chunks = []

for index, chunk in enumerate(chunks, start=1):
    tamanho = len(chunk.page_content)

    if tamanho < 100:
        small_chunks.append(
            {
                "chunk": index,
                "tamanho": tamanho,
                "source": chunk.metadata.get("source")
            }
        )

if small_chunks:
    print("Chunks pequenos encontrados:")
    for item in small_chunks:
        print(item)
else:
    print("Nenhum chunk pequeno encontrado.")


# Procurar possíveis palavras grudadas
print("\n3. POSSÍVEIS ERROS DE ESPAÇAMENTO")
print("-" * 60)

problemas = []

padroes = [
    "soluçõesdigitais",
    "nodesenvolvimento",
    "comfoco",
    "tecnologia.A",
    "profissionalpor"
]


for index, chunk in enumerate(chunks, start=1):

    texto = chunk.page_content

    for padrao in padroes:
        if padrao in texto:
            problemas.append(
                {
                    "chunk": index,
                    "problema": padrao,
                    "source": chunk.metadata.get("source")
                }
            )


if problemas:
    print("Possíveis problemas encontrados:")
    for item in problemas:
        print(item)
else:
    print("Nenhum padrão problemático encontrado.")


# Estatísticas
print("\n4. ESTATÍSTICAS")
print("-" * 60)

tamanhos = [len(chunk.page_content) for chunk in chunks]

print("Menor chunk:", min(tamanhos), "caracteres")
print("Maior chunk:", max(tamanhos), "caracteres")
print("Média:", round(sum(tamanhos) / len(tamanhos), 2), "caracteres")


print("\n" + "=" * 60)
print("TESTE FINALIZADO")
print("=" * 60)
