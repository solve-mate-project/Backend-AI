from typing import Dict, Optional, Type

from src.domain.entities.problem import PlatformType
from src.domain.repositories.problem_repository import ProblemRepository
from src.infrastructure.repositories.programmers_problem_repository import (
    ProgrammersProblemRepository,
)
from src.infrastructure.repositories.baekjoon_problem_repository import (
    BaekjoonProblemRepository,
)
from src.infrastructure.repositories.leetcode_problem_repository import (
    LeetcodeProblemRepository,
)


class ProblemRepositoryFactory:
    """플랫폼 타입에 맞는 저장소를 생성하는 팩토리 클래스"""

    def __init__(self):
        self._repositories: Dict[PlatformType, ProblemRepository] = {}
        self._register_default_repositories()

    def _register_default_repositories(self):
        """기본 저장소들을 등록합니다."""
        self.register_repository(
            PlatformType.PROGRAMMERS, ProgrammersProblemRepository()
        )
        self.register_repository(PlatformType.BAEKJOON, BaekjoonProblemRepository())
        self.register_repository(PlatformType.LEETCODE, LeetcodeProblemRepository())

    def register_repository(
        self, platform_type: PlatformType, repository: ProblemRepository
    ):
        """특정 플랫폼 타입에 대한 저장소를 등록합니다."""
        self._repositories[platform_type] = repository

    def get_repository(
        self, platform_type: PlatformType
    ) -> Optional[ProblemRepository]:
        """특정 플랫폼 타입에 대한 저장소를 반환합니다."""
        return self._repositories.get(platform_type)
