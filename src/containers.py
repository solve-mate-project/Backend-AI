from dependency_injector import containers, providers
from dependency_injector.providers import (
    Callable,
    Configuration,
)

from src.infrastructure.llm.ollama_client import OllamaClient
from src.infrastructure.repositories.difficulty_log_repository_impl import (
    DifficultyLogRepositoryImpl,
)
from src.infrastructure.repositories.problem_repository_factory import (
    ProblemRepositoryFactory,
)
from src.application.usecases.predict_problem_difficulty import (
    PredictProblemDifficultyUseCase,
)
from src.infrastructure.services.LLMDifficultyPredictor import (
    LLMDifficultyPredictor,
)


class Container(containers.DeclarativeContainer):
    """의존성 주입을 위한 컨테이너"""
    config = Configuration(yaml_files=["config.yaml"])

    # 인프라스트럭처 계층 의존성
    ollama_client = providers.Singleton(OllamaClient)
    problem_repository_factory = providers.Singleton(ProblemRepositoryFactory)
    difficulty_log_repository = providers.Singleton(
        DifficultyLogRepositoryImpl, session=database.provided.session
    )

    difficulty_predictor = providers.Singleton(
        LLMDifficultyPredictor,
        llm_client=ollama_client,
        model_name=config.llm_model_name,
    )

    # 유스케이스 의존성
    predict_difficulty_usecase = providers.Singleton(
        PredictProblemDifficultyUseCase,
        problem_repository_factory=problem_repository_factory,
        difficulty_predictor=difficulty_predictor,
    )
