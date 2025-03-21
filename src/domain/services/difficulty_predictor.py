from abc import ABC, abstractmethod
from typing import Tuple

from src.domain.entities.problem import DifficultyLevel, Problem


class DifficultyPredictor(ABC):
    @abstractmethod
    async def predict_difficulty(self, problem: Problem) -> Tuple[DifficultyLevel, str]:
        """문제의 난이도를 예측하고 설명과 함께 반환합니다."""
        pass

    @property
    def model_name(self) -> str:
        """사용된 모델의 이름을 반환합니다. 모델이 없는 경우 'unknown'을 반환할 수 있습니다."""
        return "unknown"  # 기본값
