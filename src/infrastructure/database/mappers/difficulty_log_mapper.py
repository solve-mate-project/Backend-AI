from datetime import datetime
from src.domain.entities.problem import Problem
from src.infrastructure.database.models.difficulty_log_model import DifficultyLogModel


class DifficultyLogMapper:
    @staticmethod
    def entity_to_db_model(problem: Problem, model_version: str) -> DifficultyLogModel:
        """
        Problem 엔티티를 DifficultyLogModel로 변환합니다.

        Args:
            problem: 난이도가 예측된 문제 객체
            model_version: 사용된 예측 모델 버전(선택사항)

        Returns:
            DifficultyLogModel: DB에 저장할 모델 객체
        """

        return DifficultyLogModel(
            platform=problem.platform.value,
            title=problem.title,
            difficulty=problem.difficulty.value,
            difficulty_explanation=problem.difficulty_explanation,
            prediction_date=datetime.now(),
            model_version=model_version,
        )
