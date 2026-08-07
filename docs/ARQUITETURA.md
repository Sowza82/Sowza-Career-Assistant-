# Arquitetura do Sowza Career Assistant

## Visão Geral

O Sowza Career Assistant é um agente de Inteligência Artificial baseado em RAG
(Retrieval-Augmented Generation).

O objetivo do sistema é responder perguntas sobre a trajetória profissional de
Tatiane Souza utilizando uma base de conhecimento própria contendo documentos
estruturados em Markdown.

O agente combina recuperação de informações relevantes com geração de respostas
por modelo de linguagem, permitindo respostas contextualizadas e baseadas em
dados reais.

---

## Arquitetura RAG

O funcionamento do sistema segue o fluxo:

```
Documentos Markdown
        |
        ↓
      Loader
        |
        ↓
     Splitter
        |
        ↓
    Embeddings
        |
        ↓
     ChromaDB
        |
        ↓
    Retriever
        |
        ↓
  Prompt + Gemini LLM
        |
        ↓
  Resposta ao usuário
```

---

## Fluxo do Sistema

### 1. Base de Conhecimento

Os documentos profissionais são armazenados em:

```
data/raw/knowledge-base/
```

Exemplos:

- formação;
- certificações;
- habilidades técnicas;
- projetos;
- experiência profissional;
- objetivos profissionais.

Os arquivos são escritos em Markdown para facilitar manutenção e evolução.

---

### 2. Carregamento dos Documentos

Arquivo responsável:

```
src/loader.py
```

Responsabilidade:

- localizar documentos Markdown;
- carregar os arquivos;
- transformar em documentos processáveis pelo LangChain.

---

### 3. Divisão em Chunks

Arquivo responsável:

```
src/splitter.py
```

Responsabilidade:

- dividir documentos grandes em partes menores;
- preservar contexto;
- preparar os textos para geração dos embeddings.

Configuração:

```
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
```

---

### 4. Geração de Embeddings

Arquivo responsável:

```
src/embeddings.py
```

Responsabilidade:

- transformar textos em vetores numéricos;
- utilizar o modelo de embeddings do Google Gemini.

Modelo utilizado:

```
models/gemini-embedding-001
```

---

### 5. Banco Vetorial

Arquivo responsável:

```
src/vector_store.py
```

Responsabilidade:

- armazenar embeddings;
- realizar busca semântica;
- utilizar ChromaDB como banco vetorial.

---

### 6. Recuperação de Contexto

Arquivo responsável:

```
src/retriever.py
```

Responsabilidade:

- receber a pergunta do usuário;
- buscar os documentos mais relevantes;
- retornar contexto para o modelo de linguagem.

Configuração:

```
TOP_K = 3
SEARCH_TYPE = similarity
```

---

### 7. Modelo de Linguagem

Arquivo responsável:

```
src/llm.py
```

Responsabilidade:

- configurar o modelo Gemini;
- gerar respostas utilizando o contexto recuperado.

Modelo:

```
gemini-3.6-flash
```

---

### 8. Engenharia de Prompt

Arquivo responsável:

```
src/prompts.py
```

Responsabilidade:

Definir:

- identidade do assistente;
- regras de resposta;
- limitações;
- comportamento profissional;
- segurança contra respostas fora do contexto.

---

### 9. Pipeline Principal

Arquivo responsável:

```
src/rag_pipeline.py
```

Responsabilidade:

Orquestrar todo o fluxo:

1. Receber pergunta;
2. Buscar contexto;
3. Montar prompt;
4. Enviar para Gemini;
5. Retornar resposta final.

Função principal:

```python
ask(question)
```

---

## Estrutura do Projeto

```
src/
│
├── __init__.py
├── config.py
├── loader.py
├── splitter.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── llm.py
├── prompts.py
├── rag_pipeline.py
└── utils.py
```

---

## Testes Automatizados

O projeto possui uma suíte de testes utilizando Pytest.

Atualmente:

```
46 testes passando
```

Os testes validam:

- configurações;
- carregamento de documentos;
- embeddings;
- banco vetorial;
- retriever;
- prompts;
- pipeline RAG;
- funções auxiliares.

---

## Tecnologias Utilizadas

- Python
- LangChain
- Google Gemini
- ChromaDB
- Pytest
- python-dotenv
- Markdown

---

## Versão Atual

```
Sowza Career Assistant v2.0
```

Características:

- arquitetura modular;
- pipeline RAG funcional;
- testes automatizados;
- documentação técnica;
- preparado para evolução futura.