import re
from typing import Tuple

from src.domain.entities.problem import DifficultyLevel, Problem
from src.domain.services.difficulty_predictor import DifficultyPredictor
from src.infrastructure.llm.llm_client import LLMClient


class LLMDifficultyPredictor(DifficultyPredictor):
    def __init__(self, llm_client: LLMClient, model_name: str):
        self._llm_client = llm_client
        self._model_name = model_name

    async def predict_difficulty(self, problem: Problem) -> Tuple[DifficultyLevel, str]:
        try:
            # 플랫폼에 따라 프롬프트 조정
            platform_name = problem.platform

            # Prompt 생성
            prompt = f"""
            The following is a coding problem from {platform_name}. Please evaluate its difficulty as EASY, NORMAL, or HARD.

            EASY: Basic algorithm problems that beginners can solve
            NORMAL: Medium difficulty problems that require moderate algorithm knowledge and experience
            HARD: Difficult problems that require advanced algorithm knowledge or optimization techniques

            Please provide only the difficulty level (EASY, NORMAL, or HARD) and a brief explanation of your assessment.

            Title: {problem.title}

            Problem Content:
            {problem.content[:1500]}

            Difficulty Assessment (EASY/NORMAL/HARD):
            """

            # LLM 클라이언트를 통해 모델 호출
            response = self._llm_client.chat(
                model=self.model_name, messages=[{"role": "user", "content": prompt}]
            )

            # 응답 처리
            response_text = response["message"]["content"].strip()

            # 난이도 추출 로직 (기존과 동일)
            level_pattern = re.search(
                r"(EASY|NORMAL|HARD)", response_text, re.IGNORECASE
            )
            if level_pattern:
                difficulty = level_pattern.group(1).upper()
                return DifficultyLevel(difficulty), response_text.strip()

            response_lower = response_text.lower()
            if (
                "easy" in response_lower
                or "쉬운" in response_lower
                or "간단" in response_lower
            ):
                difficulty = DifficultyLevel.EASY
            elif (
                "hard" in response_lower
                or "어려운" in response_lower
                or "복잡" in response_lower
            ):
                difficulty = DifficultyLevel.HARD
            else:
                difficulty = DifficultyLevel.NORMAL

            return difficulty, response_text.strip()

        except Exception as e:
            return DifficultyLevel.ERROR, f"레벨 예측 중 오류 발생: {str(e)}"

    @property
    def model_name(self) -> str:
        return self._model_name
