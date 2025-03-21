from typing import Protocol


class LLMClient(Protocol):
    """
    LLMClient를 Protocol로 정의하면, ollama뿐만 아니라
    openai, huggingface 등 다양한 LLM 클라이언트를 사용할 수 있습니다.
    이들은 각기 다른 구현체일 수 있지만, chat 메서드만 제공하면 동작하도록 보장합니다.
    """

    def chat(self, model: str, messages: list):
        pass
