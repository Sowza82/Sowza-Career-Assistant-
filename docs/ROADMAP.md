# Roadmap — Sowza Career Assistant

## Visão Geral

O Sowza Career Assistant é um agente de inteligência artificial baseado em RAG (Retrieval-Augmented Generation), criado para responder perguntas sobre a trajetória profissional de Tatiane Souza utilizando uma base de conhecimento personalizada.

A evolução do projeto foi organizada em versões, permitindo crescimento gradual da aplicação, priorizando primeiro a estabilidade técnica e posteriormente novos recursos inteligentes.

---

## Versão 1.0 — Protótipo RAG

### Objetivo

Criar a primeira versão funcional do assistente utilizando arquitetura RAG.

### Desenvolvimento realizado

A versão inicial foi construída em ambiente experimental utilizando Google Colab.

Principais etapas:

- Criação da base de conhecimento;
- Organização dos documentos profissionais;
- Leitura dos arquivos Markdown;
- Divisão dos documentos em chunks;
- Geração dos embeddings;
- Criação do banco vetorial;
- Implementação do mecanismo de recuperação;
- Integração com modelo Gemini.

### Tecnologias utilizadas

- Python;
- Google Colab;
- LangChain;
- Google Gemini;
- Google Embedding;
- ChromaDB.

### Resultado

Foi criado um protótipo funcional capaz de recuperar informações da base de conhecimento e gerar respostas utilizando contexto relevante.

---

## Versão 2.0 — Arquitetura Modular e Qualidade

### Objetivo

Transformar o protótipo inicial em uma aplicação organizada, escalável e preparada para evolução.

### Melhorias implementadas

#### Organização do projeto

Separação das responsabilidades em módulos:

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

---

#### Pipeline RAG estruturado

Fluxo atual:

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
   Vector Store
        |
        ↓
    Retriever
        |
        ↓
      Prompt
        |
        ↓
      Gemini
        |
        ↓
     Resposta
```

---

#### Testes automatizados

Foi criada uma suíte utilizando Pytest.

Cobertura:

- Configurações;
- Embeddings;
- Modelo LLM;
- Loader;
- Metadata;
- Prompts;
- Qualidade dos documentos;
- Retriever;
- Splitter;
- Vector Store;
- Pipeline RAG;
- Utils.

Resultado atual:

```
46 testes executados
46 testes aprovados
```

---

## Versão 3.0 — Assistente Adaptativo

### Objetivo

Adicionar inteligência personalizada ao assistente.

A aplicação deixará de apenas responder perguntas sobre a trajetória profissional e passará a adaptar suas respostas conforme o perfil do usuário.

---

### Funcionalidades planejadas

#### Perfil do usuário

Criar uma camada de contexto contendo:

- Área profissional;
- Objetivos;
- Nível de conhecimento;
- Preferências de aprendizado.

---

#### Respostas personalizadas

Exemplos:

Usuário iniciante:

- Explicações mais didáticas;
- Menos termos técnicos;
- Exemplos práticos.

Usuário avançado:

- Detalhes de arquitetura;
- Decisões técnicas;
- Código e implementação.

---

#### Memória conversacional

Adicionar capacidade de:

- Manter contexto entre perguntas;
- Registrar histórico;
- Melhorar continuidade da conversa.

---

## Versão 4.0 — Plataforma de Carreira Inteligente

### Objetivo

Transformar o assistente em uma plataforma completa de apoio profissional.

Possíveis funcionalidades:

- Análise de currículo;
- Preparação para entrevistas;
- Simulação de entrevistas técnicas;
- Avaliação de vagas;
- Sugestões de melhoria profissional;
- Trilhas personalizadas de estudo;
- Integração com portfólio.

---

## Interface e Experiência do Usuário

### Planejamento futuro

Após a consolidação da parte funcional, será criada uma interface profissional.

Possíveis tecnologias:

- Streamlit;
- React;
- Next.js.

Objetivos:

- Interface de chat;
- Identidade visual SowzaTech;
- Melhor experiência de navegação;
- Apresentação profissional do projeto.

---

## Deploy e Produção

### Planejamento

Disponibilizar o assistente em ambiente cloud.

Possíveis plataformas:

- Oracle Cloud Infrastructure;
- Google Cloud;
- AWS.

Objetivos:

- Aplicação acessível online;
- Melhor disponibilidade;
- Estrutura preparada para crescimento.

---

## Histórico de Versões

| Versão | Status | Descrição |
|---|---|---|
| 1.0 | Concluída | Protótipo RAG funcional |
| 2.0 | Concluída | Arquitetura modular e testes automatizados |
| 3.0 | Planejada | Assistente adaptativo |
| 4.0 | Futuro | Plataforma inteligente de carreira |

---

## Estratégia de Evolução

A evolução do Sowza Career Assistant seguirá três princípios:

1. Construir uma base técnica sólida;
2. Garantir qualidade antes de adicionar complexidade;
3. Evoluir gradualmente para uma solução inteligente e profissional.

Cada versão representa uma etapa do amadurecimento do projeto.