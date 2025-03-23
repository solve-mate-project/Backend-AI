from src.domain.entities.problem import Problem
from src.domain.repositories.difficulty_log_repository import DifficultyLogRepository
from src.infrastructure.database.mappers.difficulty_log_mapper import (
    DifficultyLogMapper,
)


class DifficultyLogRepositoryImpl(DifficultyLogRepository):
    def __init__(self, session_factory) -> None:
        self.__session_factory = session_factory

    async def save_difficulty_prediction_log(
        self, problem: Problem, model_name: str
    ) -> None:
        """
        난이도 예측 로그를 DB에 저장합니다.
        """
        with self.__session_factory() as session:
            record = DifficultyLogMapper.entity_to_db_model(problem, model_name)
            session.add(record)
            session.commit()
            session.refresh(record)
