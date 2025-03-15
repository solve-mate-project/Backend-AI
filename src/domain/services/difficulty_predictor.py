from abc import ABC, abstractmethod
from typing import Tuple

from src.domain.entities.problem import DifficultyLevel, Problem


class DifficultyPredictor(ABC):
    @abstractmethod
    async def predict_difficulty(self, problem: Problem) -> Tuple[DifficultyLevel, str]:
        """문제의 난이도를 예측하고 설명과 함께 반환합니다."""
        pass
