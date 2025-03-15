import re
from typing import Optional

import requests
from bs4 import BeautifulSoup

from src.domain.entities.problem import Problem, PlatformType
from src.domain.repositories.problem_repository import ProblemRepository


class BaekjoonProblemRepository(ProblemRepository):
    async def get_problem_by_url(self, url: str) -> Optional[Problem]:
        """백준 URL을 받아 문제 정보를 파싱합니다."""
        # URL 유효성 검사
        if not re.match(r"https://www\.acmicpc\.net/problem/\d+", url):
            return None

        try:
            # 웹 페이지 요청
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            # BeautifulSoup으로 HTML 파싱
            soup = BeautifulSoup(response.text, "html.parser")

            # 문제 제목 추출
            title_element = soup.select_one("#problem_title")
            title = (
                title_element.text.strip()
                if title_element
                else "제목을 찾을 수 없습니다"
            )

            # 문제 내용 추출
            content_element = soup.select_one("#problem-body")
            problem_content = ""
            if content_element:
                # HTML 태그 제거하고 텍스트만 추출
                problem_content = content_element.get_text(separator="\n", strip=True)

            # Problem 엔티티 생성
            return Problem(
                title=title,
                content=problem_content,
                platform=PlatformType.BAEKJOON,
                url=url,
            )
        except Exception:
            return None
