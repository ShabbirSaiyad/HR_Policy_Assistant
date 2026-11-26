"""All settings for the app live here, in one place."""


import os
from dotenv import load_dotenv

# Project root folder (the one that contains data/, .env, app.py).
# All paths are built from here so the app works no matter which
# folder you run it from.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

## ENV VAR - LLMS 

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

# Tracing
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")

# GUARD MODEL 

GUARD_MODEL_NAME = "openai/gpt-oss-safeguard-20b"


## DEFINE PATH - DATA / VECTOR STORE 

DATA_FILE_PATH = os.path.join(PROJECT_ROOT, "data", "hr_policy.txt")

## VECTORE STORES 

# IN MEMORY 
# persistent memory - vectors # 100gb - ingestion 
# cloud memory 
VECTOR_STORE_PATH = os.path.join(PROJECT_ROOT, "data", "faiss_index")

## MODELS 
# LLM and EMBEDING MODEL 

LLM_MODEL_NAME = "openai/gpt-oss-20b"

EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"

## CHUNK / TEXT SPLITTING CONFIG 

CHUNK_SIZE = 500
CHUNK_OVERLAP = 60

# RETRIVAL RESULTS 
TOP_K_RESULTS = 3


## SYSTEM INSTRUCTIONS 

SYSTEM_PROMPT = (
    "You are a friendly HR assistant. Always use the search_hr_policy tool to look up "
    "facts before answering. If the answer isn't in the search results, say you don't know "
    "instead of guessing."
)


def check_api_keys() -> None:
    """Stop early with a clear message if a required API key is missing."""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Please add it to your .env file.")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY. Please add it to your .env file.")
