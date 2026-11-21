from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

@lru_cache
def load_llm():
    return init_chat_model(model = 'openai:gpt-4o')