import ollama
from .llm_client import LLMClient


class OllamaClient(LLMClient):
    def chat(self, model: str, messages: list) -> ollama.ChatResponse:
        return ollama.chat(model=model, messages=messages)
