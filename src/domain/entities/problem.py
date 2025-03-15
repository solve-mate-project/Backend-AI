from dataclasses import dataclass
from enum import Enum
from typing import Optional


class DifficultyLevel(str, Enum):
    EASY = "EASY"
    NORMAL = "NORMAL"
    HARD = "HARD"
    ERROR = "ERROR"


class PlatformType(str, Enum):
    PROGRAMMERS = "programmers"
    BAEKJOON = "baekjoon"
    LEETCODE = "leetcode"
    UNKNOWN = "unknown"


@dataclass
class Problem:
    title: str
    content: str
    platform: PlatformType
    url: str
    difficulty: Optional[DifficultyLevel] = None
    difficulty_explanation: Optional[str] = None
