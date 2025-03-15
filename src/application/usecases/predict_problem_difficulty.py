from typing import Optional

from src.domain.entities.problem import Problem
from src.domain.repositories.problem_repository import ProblemRepository
from src.domain.services.difficulty_predictor import DifficultyPredictor
from src.infrastructure.repositories.problem_repository_factory import (
    ProblemRepositoryFactory,
)


class PredictProblemDifficultyUseCase:
    def __init__(
        self,
        problem_repository_factory: ProblemRepositoryFactory,
        difficulty_predictor: DifficultyPredictor,
    ):
        self._problem_repository_factory = problem_repository_factory
        self._difficulty_predictor = difficulty_predictor

    async def execute(self, url: str) -> Optional[Problem]:
        """
        문제 URL을 받아 문제 정보를 가져오고 난이도를 예측합니다.

        Args:
            url: 문제 URL

        Returns:
            Problem: 난이도가 예측된 문제 객체
        """
        # URL에서 플랫폼 판단
        platform = ProblemRepository.determine_platform(url)

        # 플랫폼에 맞는 저장소 가져오기
        repository = self._problem_repository_factory.get_repository(platform)

        if not repository:
            return None

        # 문제 정보 가져오기
        problem = await repository.get_problem_by_url(url)

        if not problem:
            return None

        # 난이도 예측
        difficulty, explanation = await self._difficulty_predictor.predict_difficulty(
            problem
        )

        # 결과 업데이트
        problem.difficulty = difficulty
        problem.difficulty_explanation = explanation

        return problem
