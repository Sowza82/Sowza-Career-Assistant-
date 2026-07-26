# 🚀 Sowza Career Assistant

> Um agente de Inteligência Artificial baseado em **RAG (Retrieval-Augmented Generation)** capaz de responder perguntas sobre minha trajetória profissional utilizando uma base de conhecimento personalizada.

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Sobre o Projeto

O **Sowza Career Assistant** é um projeto desenvolvido para o **Challenge Alura Agente 2026**.

A proposta é construir um agente inteligente utilizando a arquitetura **RAG (Retrieval-Augmented Generation)**, permitindo que a IA consulte uma base de conhecimento antes de responder às perguntas.

Diferentemente de um chatbot tradicional, este agente responde utilizando informações documentadas sobre minha trajetória profissional, tornando as respostas mais precisas e contextualizadas.

---

# 🎯 Objetivos

O projeto tem como objetivos:

- Desenvolver um agente utilizando RAG.
- Aplicar conceitos de Inteligência Artificial Generativa.
- Construir uma base vetorial utilizando ChromaDB.
- Utilizar o Google Gemini como modelo de linguagem.
- Criar uma interface utilizando Streamlit.
- Publicar a aplicação na Oracle Cloud Infrastructure (OCI).
- Demonstrar conhecimentos técnicos por meio de um projeto autoral.

---

# 🧠 Base de Conhecimento

A base de conhecimento foi construída utilizando documentos em Markdown organizados por assunto.

Atualmente ela contém:

- Sobre Mim
- Formação
- Certificações
- Habilidades Técnicas
- Projetos
- Experiências
- Portfólio
- Contato
- Objetivos Profissionais
- Sowza.dev
- FAQ
- Glossário

Esses documentos serão processados para geração dos embeddings utilizados pelo agente.

---

# 🏗 Arquitetura

Fluxo simplificado do projeto:

```text
Documentos (.md)
        │
        ▼
Leitura dos arquivos
        │
        ▼
Chunking
        │
        ▼
Embeddings (Google Gemini)
        │
        ▼
ChromaDB
        │
        ▼
Retriever
        │
        ▼
LLM (Google Gemini)
        │
        ▼
Resposta ao usuário
```

---

# 🛠 Tecnologias

- Python
- Google Gemini
- LangChain
- ChromaDB
- Streamlit
- Google Colab
- Oracle Cloud Infrastructure (OCI)
- Git
- GitHub

---

# 📂 Estrutura do Projeto

```text
sowza-career-assistant/
│
├── knowledge-base/
│   ├── 01_sobre_mim.md
│   ├── 02_formacao.md
│   ├── 03_certificacoes.md
│   ├── 04_habilidades_tecnicas.md
│   ├── 05_projetos.md
│   ├── 06_experiencias.md
│   ├── 07_portfolio.md
│   ├── 08_contato.md
│   ├── 09_objetivos_profissionais.md
│   ├── 10_sowzatech.md
│   ├── 11_faq.md
│   └── 12_glossario.md
│
├── notebooks/
├── src/
├── chroma_db/
├── README.md
└── requirements.txt
```

---

# 🚀 Roadmap

- [x] Planejamento do projeto
- [x] Definição da arquitetura
- [x] Criação da base de conhecimento
- [ ] Protótipo no Google Colab
- [ ] Chunking dos documentos
- [ ] Geração dos embeddings
- [ ] Banco vetorial (ChromaDB)
- [ ] Pipeline RAG
- [ ] Interface com Streamlit
- [ ] Deploy na Oracle Cloud
- [ ] Documentação final

---

# 💻 Como executar

> Em desenvolvimento.

Em breve serão disponibilizadas instruções completas para instalação e execução do projeto.

---

# 📸 Demonstração

Em desenvolvimento.

---

# 📚 Aprendizados

Este projeto está sendo desenvolvido com foco em aprofundar conhecimentos em:

- Inteligência Artificial Generativa
- Retrieval-Augmented Generation (RAG)
- Engenharia de Prompt
- LangChain
- Banco Vetorial
- Google Gemini
- Streamlit
- Oracle Cloud Infrastructure

---

# 👩‍💻 Desenvolvedora

**Tatiane Souza**

**Sowza.tech**

GitHub:
<https://github.com/Sowza82>

LinkedIn:
<https://www.linkedin.com/in/tatiane-souza-tech>

---

# 📄 Licença

Este projeto está licenciado sob a licença MIT.
