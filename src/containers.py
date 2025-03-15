from dependency_injector import containers, providers

from src.infrastructure.repositories.problem_repository_factory import (
    ProblemRepositoryFactory,
)
from src.application.usecases.predict_problem_difficulty import (
    PredictProblemDifficultyUseCase,
)
from src.infrastructure.services.ollama_difficulty_predictor import (
    OllamaDifficultyPredictor,
)


class Container(containers.DeclarativeContainer):
    """의존성 주입을 위한 컨테이너"""

    # 인프라스트럭처 계층 의존성
    problem_repository_factory = providers.Singleton(ProblemRepositoryFactory)
    difficulty_predictor = providers.Singleton(OllamaDifficultyPredictor)

    # 유스케이스 의존성
    predict_difficulty_usecase = providers.Singleton(
        PredictProblemDifficultyUseCase,
        problem_repository_factory=problem_repository_factory,
        difficulty_predictor=difficulty_predictor,
    )
