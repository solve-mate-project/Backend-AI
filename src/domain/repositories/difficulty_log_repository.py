from typing import Optional

from src.domain.entities.problem import Problem


class DifficultyLogRepository:
    """난이도 예측 로그를 저장하는 레포지토리 인터페이스"""

    async def save_difficulty_prediction_log(
        self, problem: Problem, model_name: str
    ) -> None:
        """
        난이도 예측 로그를 저장합니다.

        Args:
            problem: 난이도가 예측된 문제 객체
            model_version: 사용된 예측 모델 버전(선택사항)
        """
        pass
