# Changelog

Histórico de evolução do Sowza Career Assistant.

Todas as mudanças relevantes do projeto são registradas neste arquivo.

---

## Versão 2.0

Data: Agosto de 2026

### Resumo

A versão 2.0 representa a evolução do protótipo inicial para uma aplicação
Python estruturada, modular e testável.

O projeto deixou de ser apenas uma prova de conceito em notebook e passou a
possuir uma arquitetura organizada de agente RAG.

---

### Adicionado

#### Estrutura da Aplicação

- Organização do projeto em módulos Python;
- Criação da pasta `src/`;
- Separação das responsabilidades de cada componente;
- Criação do pacote principal com `__init__.py`.

---

#### Pipeline RAG Completo

Implementado o fluxo:

```
Documentos
    ↓
  Loader
    ↓
 Splitter
    ↓
Embeddings
    ↓
 ChromaDB
    ↓
Retriever
    ↓
  Gemini
    ↓
 Resposta
```

---

#### Módulos Criados

##### config.py

Responsável por:

- variáveis de ambiente;
- caminhos do projeto;
- configuração dos modelos;
- parâmetros do RAG.

---

##### loader.py

Responsável por:

- localizar documentos Markdown;
- carregar a base de conhecimento.

---

##### splitter.py

Responsável por:

- dividir documentos em chunks;
- controlar tamanho e sobreposição.

Configuração:

```
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
```

---

##### embeddings.py

Responsável por:

- geração de embeddings;
- integração com Google Gemini Embeddings.

Modelo utilizado:

```
models/gemini-embedding-001
```

---

##### vector_store.py

Responsável por:

- criação do banco vetorial;
- integração com ChromaDB.

---

##### retriever.py

Responsável por:

- busca semântica;
- recuperação dos documentos relevantes.

---

##### llm.py

Responsável pela integração com o modelo Gemini.

Modelo:

```
gemini-3.6-flash
```

---

##### prompts.py

Implementada engenharia de prompt contendo:

- identidade do assistente;
- regras de comportamento;
- limitações;
- segurança;
- contexto profissional.

---

##### rag_pipeline.py

Criado o pipeline principal:

```python
ask(question)
```

Responsável por integrar:

- Retriever;
- Prompt;
- LLM;
- Resposta final.

---

##### utils.py

Criadas funções auxiliares para:

- normalização de textos;
- validação de perguntas;
- processamento auxiliar.

---

### Testes Automatizados

Foi criada uma suíte completa utilizando Pytest.

Resultado atual:

```
46 testes passando
```

Cobertura:

- configurações;
- embeddings;
- LLM;
- carregamento;
- metadados;
- prompts;
- qualidade dos documentos;
- pipeline RAG;
- retriever;
- splitter;
- vector store;
- utilitários.

---

### Melhorias Técnicas

Implementado:

- código modular;
- separação de responsabilidades;
- documentação dos módulos;
- validação automatizada;
- tratamento de configurações.

---

## Versão 1.0

### Resumo

Primeira versão experimental desenvolvida durante o Challenge Alura Agente.

Objetivo:

Criar um agente capaz de responder perguntas sobre trajetória profissional
utilizando documentos próprios.

---

### Implementado

- Criação da base de conhecimento;
- Organização dos documentos Markdown;
- Testes iniciais no Google Colab;
- Geração de chunks;
- Criação de embeddings;
- Banco vetorial ChromaDB;
- Primeiro fluxo RAG funcional.

---

### Ambiente Inicial

Protótipo desenvolvido utilizando:

- Google Colab;
- Python;
- LangChain;
- Google Gemini;
- ChromaDB.

---

## Próximas Versões

### Versão 3.0 (Planejada)

Possíveis evoluções:

- interface web;
- experiência visual profissional;
- memória de usuário;
- respostas adaptativas baseadas em perfil;
- deploy em nuvem;
- melhorias de arquitetura.

---

## Observação

O projeto segue evolução incremental.

Cada versão prioriza:

1. funcionamento;
2. estabilidade;
3. organização;
4. experiência do usuário.