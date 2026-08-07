# Instalação e Configuração

## Sowza Career Assistant

Este documento apresenta o processo de instalação e configuração do ambiente
necessário para executar o Sowza Career Assistant localmente.

Versão atual:

```
2.0
```

---

## Requisitos

Antes de iniciar, é necessário possuir:

- Python 3.12 ou superior;
- Git instalado;
- Conta Google com acesso à API Gemini;
- Chave de API do Google AI Studio.

---

## Clonar o Projeto

Execute:

```bash
git clone https://github.com/Sowza82/Sowza-Career-Assistant-.git
```

Acesse o diretório:

```bash
cd Sowza-Career-Assistant-
```

---

## Criar Ambiente Virtual

Criar o ambiente:

```bash
python -m venv venv
```

Ativar ambiente virtual.

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Após ativação, o terminal deverá apresentar:

```
(venv)
```

---

## Instalação das Dependências

Instalar os pacotes:

```bash
pip install -r requirements.txt
```

Principais tecnologias instaladas:

- LangChain;
- Google Generative AI;
- ChromaDB;
- Pytest;
- python-dotenv.

---

## Configuração da API Gemini

O projeto utiliza uma variável de ambiente para armazenar a chave da API.

Criar um arquivo:

```
.env
```

Na raiz do projeto.

Adicionar:

```
GOOGLE_API_KEY=sua_chave_aqui
```

A chave deve ser obtida no Google AI Studio.

---

## Estrutura das Pastas Principais

Após instalação, o projeto deve possuir:

```
Sowza-Career-Assistant-

├── data/
│   └── raw/
│       └── knowledge-base/

├── docs/

├── src/

├── tests/

├── .env

├── requirements.txt

└── README.md
```

---

## Executando o Projeto

### Testando os módulos

Executar todos os testes:

```bash
pytest tests/ -v
```

Resultado esperado:

```
46 passed
```

---

### Executando o Pipeline RAG

O pipeline principal está localizado em:

```
src/rag_pipeline.py
```

A função principal:

```
ask(question)
```

Recebe uma pergunta e retorna uma resposta baseada na base de conhecimento.

Exemplo:

```python
from src.rag_pipeline import ask

response = ask(
    "Quem é Tatiane Souza?"
)

print(response)
```

---

## Fluxo de Execução

O sistema executa:

```
Pergunta do usuário
        |
        ↓
Retriever busca contexto
        |
        ↓
Documentos relevantes
        |
        ↓
Prompt do sistema
        |
        ↓
Gemini LLM
        |
        ↓
Resposta final
```

---

## Solução de Problemas

### Erro: GOOGLE_API_KEY ausente

Verifique:

- se o arquivo `.env` existe;
- se a variável está escrita corretamente;
- se a chave é válida.

### Erro de dependências

Atualizar o ambiente:

```bash
pip install --upgrade pip
```

Depois:

```bash
pip install -r requirements.txt
```

---

## Testes Automatizados

A versão 2.0 possui:

```
46 testes automatizados
```

Eles garantem o funcionamento dos principais componentes:

- configuração;
- carregamento;
- processamento;
- embeddings;
- armazenamento vetorial;
- recuperação;
- geração de respostas.

---

## Próximas Evoluções

Planejadas:

- interface web;
- melhorias de experiência do usuário;
- deploy em cloud;
- personalização adaptativa das respostas.