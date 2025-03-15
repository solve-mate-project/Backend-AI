import re
import json
from typing import Optional

import requests
from bs4 import BeautifulSoup

from src.domain.entities.problem import Problem, PlatformType
from src.domain.repositories.problem_repository import ProblemRepository


class LeetcodeProblemRepository(ProblemRepository):
    async def get_problem_by_url(self, url: str) -> Optional[Problem]:
        """리트코드 URL을 받아 문제 정보를 파싱합니다."""
        # URL 유효성 검사
        match = re.match(r"https://leetcode\.com/problems/([\w-]+)", url)
        if not match:
            return None

        problem_slug = match.group(1)

        try:
            # GraphQL API를 사용하여 문제 데이터 가져오기
            graphql_url = "https://leetcode.com/graphql"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Content-Type": "application/json",
                "Referer": url,
            }

            query = """
            query questionData($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    title
                    content
                    difficulty
                }
            }
            """

            payload = {"query": query, "variables": {"titleSlug": problem_slug}}

            response = requests.post(graphql_url, headers=headers, json=payload)
            response.raise_for_status()

            data = response.json()
            question_data = data.get("data", {}).get("question", {})

            if not question_data:
                return None

            title = question_data.get("title", "제목을 찾을 수 없습니다")
            content = question_data.get("content", "내용을 찾을 수 없습니다")

            # HTML 태그 제거가 필요한 경우 BeautifulSoup 사용
            if content:
                soup = BeautifulSoup(content, "html.parser")
                content = soup.get_text(separator="\n", strip=True)

            # Problem 엔티티 생성
            return Problem(
                title=title,
                content=content,
                platform=PlatformType.LEETCODE,
                url=url,
            )
        except Exception as e:
            print(f"리트코드 문제 가져오기 오류: {str(e)}")
            return None
