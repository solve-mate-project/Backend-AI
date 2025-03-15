from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.problem import Problem, PlatformType


class ProblemRepository(ABC):
    @abstractmethod
    async def get_problem_by_url(self, url: str) -> Optional[Problem]:
        """URL로부터 문제 정보를 가져옵니다."""
        pass

    @staticmethod
    def determine_platform(url: str) -> PlatformType:
        """URL을 기반으로 플랫폼 타입을 판단합니다."""
        url_lower = url.lower()

        if "programmers.co.kr" in url_lower:
            return PlatformType.PROGRAMMERS
        elif "acmicpc.net" in url_lower or "boj" in url_lower:
            return PlatformType.BAEKJOON
        elif "leetcode.com" in url_lower:
            return PlatformType.LEETCODE
        return PlatformType.UNKNOWN
