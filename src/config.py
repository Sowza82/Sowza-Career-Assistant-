"""
============================================================
CONFIGURAÇÕES GERAIS
Sowza Career Assistant
============================================================

Centraliza todas as configurações utilizadas pelo projeto.

Versão: 2.0
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# ============================================================
# VARIÁVEIS DE AMBIENTE
# ============================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ============================================================
# DIRETÓRIOS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw" / "knowledge-base"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

VECTOR_DB_DIR = BASE_DIR / "chroma_db"

# ============================================================
# MODELOS GOOGLE
# ============================================================

LLM_MODEL = "gemini-3.6-flash"

EMBEDDING_MODEL = "models/gemini-embedding-001"

# ============================================================
# CHUNKING
# ============================================================

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

# ============================================================
# RETRIEVER
# ============================================================

TOP_K = 3

SEARCH_TYPE = "similarity"

# ============================================================
# GERAÇÃO
# ============================================================

TEMPERATURE = 0.2

MAX_OUTPUT_TOKENS = 1024