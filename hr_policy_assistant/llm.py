

from hr_policy_assistant import config
from langchain_groq import ChatGroq


def get_llm():
    """Return a Groq chat model. Reads GROQ_API_KEY from the environment."""
    return ChatGroq(model=config.LLM_MODEL_NAME, temperature=0,)