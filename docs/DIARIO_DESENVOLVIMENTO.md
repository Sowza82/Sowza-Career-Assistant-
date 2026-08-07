# Diário de Desenvolvimento — Sowza Career Assistant

## Sobre este documento

Este arquivo registra a evolução técnica do desenvolvimento do Sowza Career Assistant, documentando decisões, etapas concluídas, problemas encontrados e melhorias implementadas durante a construção do projeto.

O objetivo é manter um histórico organizado da evolução do agente de inteligência artificial baseado em RAG.

---

# Início do Projeto

## Definição da ideia

O Sowza Career Assistant nasceu com o objetivo de criar um assistente de IA capaz de responder perguntas sobre a trajetória profissional de Tatiane Souza utilizando informações personalizadas.

A proposta foi construir um agente baseado em:

* Documentos profissionais;
* Recuperação de informações;
* Modelo de linguagem generativo;
* Base de conhecimento própria.

A arquitetura escolhida foi RAG (Retrieval-Augmented Generation).

---

# Fase 1 — Preparação da Base de Conhecimento

## Organização dos documentos

Foi criada uma base de conhecimento estruturada em arquivos Markdown contendo informações profissionais.

Documentos principais:

```
data/raw/knowledge-base/

01_sobre_mim.md
02_formacao.md
03_certificacoes.md
04_habilidades_tecnicas.md
05_projetos.md
06_experiencias.md
07_portfolio.md
08_contato.md
09_objetivos_profissionais.md
10_sowzatech.md
11_faq.md
12_glossario.md
```

Objetivo:

Centralizar todas as informações utilizadas pelo assistente.

---

# Fase 2 — Construção do Protótipo RAG

## Ambiente experimental

O primeiro protótipo foi desenvolvido utilizando Google Colab.

Etapas realizadas:

* Instalação das dependências;
* Leitura dos documentos;
* Processamento dos textos;
* Criação dos chunks;
* Geração dos embeddings;
* Criação do banco vetorial;
* Testes de recuperação.

Resultado:

* 12 documentos processados;
* 84 chunks gerados;
* Banco vetorial criado;
* Recuperação de contexto funcionando.

---

# Fase 3 — Migração para Projeto Local

Após validar o protótipo, o projeto foi reorganizado para uma estrutura profissional local.

Ambiente:

* Python;
* Virtual Environment;
* Git;
* GitHub;
* VS Code.

Estrutura inicial:

```
Sowza-Career-Assistant/

src/
tests/
data/
docs/
```

---

# Fase 4 — Arquitetura Modular (Versão 2.0)

O projeto foi dividido em módulos independentes.

Estrutura:

```
src/

config.py
loader.py
splitter.py
embeddings.py
vector_store.py
retriever.py
rag_pipeline.py
llm.py
prompts.py
utils.py
```

Responsabilidades:

* `config.py`
  Centraliza configurações.

* `loader.py`
  Responsável pela leitura dos documentos.

* `splitter.py`
  Divide documentos em chunks.

* `embeddings.py`
  Gera representações vetoriais.

* `vector_store.py`
  Gerencia o banco vetorial.

* `retriever.py`
  Recupera informações relevantes.

* `rag_pipeline.py`
  Orquestra o fluxo completo.

* `llm.py`
  Configura o modelo Gemini.

* `prompts.py`
  Define regras de comportamento do assistente.

* `utils.py`
  Funções auxiliares.

---

# Fase 5 — Implementação dos Testes Automatizados

Foi criada uma suíte de testes utilizando Pytest.

Objetivo:

Garantir estabilidade durante a evolução do projeto.

Testes implementados:

* Configurações;
* Embeddings;
* LLM;
* Loader;
* Metadata;
* Prompts;
* Qualidade dos documentos;
* Retriever;
* Splitter;
* Vector Store;
* Pipeline RAG;
* Utils.

Resultado:

```
46 testes executados
46 testes aprovados
```

---

# Problemas Encontrados e Soluções

## Problema: importação do LLM

Erro encontrado:

```
ImportError: cannot import name 'create_llm'
```

Causa:

O módulo possuía a função `get_llm()` enquanto o pipeline esperava `create_llm()`.

Solução:

Padronização da chamada do modelo dentro do pipeline.

---

## Problema: resposta retornando lista

Erro:

O pipeline retornava uma estrutura de dados ao invés de texto.

Causa:

Mudança no formato de resposta do modelo Gemini.

Solução:

Tratamento da resposta para retornar somente o conteúdo textual.

---

## Problema: warnings de dependências

Warnings relacionados:

* LangChain Community;
* Configuração de parâmetros do Gemini.

Situação:

Não impedem a execução dos testes.

Tratamento futuro:

Atualização das dependências e ajustes de compatibilidade.

---

# Estado Atual do Projeto

Versão atual:

```
2.0
```

Status:

* Arquitetura modular implementada;
* Pipeline RAG funcionando;
* Testes automatizados passando;
* Base de conhecimento estruturada;
* Documentação em desenvolvimento.

---

# Próximas Etapas

Após finalizar a documentação:

* Melhorar interface do usuário;
* Criar aplicação visual;
* Preparar deploy em cloud;
* Evoluir para versão adaptativa;
* Implementar recursos inteligentes de personalização.

---

# Registro de Desenvolvimento

O Sowza Career Assistant está sendo desenvolvido de forma incremental, priorizando primeiro a construção de uma base técnica sólida e posteriormente a implementação de melhorias de experiência e inteligência.
