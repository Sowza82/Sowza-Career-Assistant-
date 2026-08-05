"""
============================================================
TESTE DO RETRIEVER
Sowza Career Assistant
============================================================

Este teste verifica se o banco vetorial pode ser
carregado corretamente e se o retriever retorna
os documentos mais relevantes para uma consulta.

Versão: 2.0
"""

from src.retriever import create_retriever

print("=" * 60)
print("TESTE DO RETRIEVER")
print("=" * 60)

retriever = create_retriever()

consulta = "Quem é Tatiane Souza?"

print(f"\nConsulta: {consulta}")

resultados = retriever.invoke(consulta)

print(f"\nQuantidade de resultados: {len(resultados)}")

print("\n" + "=" * 60)
print("DOCUMENTOS RECUPERADOS")
print("=" * 60)

for i, doc in enumerate(resultados, start=1):
    print(f"\nResultado {i}")
    print("-" * 60)

    arquivo = doc.metadata.get("source", "Desconhecido")
    print(f"Arquivo: {arquivo}")

    print("\nConteúdo:")
    print(doc.page_content[:500])
    print("...")

print("\n" + "=" * 60)
print("TESTE FINALIZADO COM SUCESSO")
print("=" * 60)
