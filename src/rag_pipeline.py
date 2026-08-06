"""
============================================================
RAG PIPELINE
Sowza Career Assistant
============================================================

Pipeline principal do sistema RAG.

Integra:

- Retriever
- Prompt
- Gemini LLM

Versão: 2.0
"""

from langchain_core.prompts import ChatPromptTemplate

from src.retriever import create_retriever
from src.llm import get_llm
from src.prompts import SYSTEM_PROMPT


def ask(question: str) -> str:
    """
    Executa todo o pipeline RAG.

    Parameters
    ----------
    question : str
        Pergunta do usuário.

    Returns
    -------
    str
        Resposta gerada pelo modelo.
    """

    retriever = create_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = ChatPromptTemplate.from_template(
        SYSTEM_PROMPT
    )

    chain = prompt | get_llm()

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    # Normaliza resposta do Gemini
    # Algumas versões retornam uma lista de blocos de texto
    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content
