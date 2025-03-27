from fastapi.testclient import TestClient


class TestPredictDifficultyEP:
    def test_predict_difficulty(self, test_client: TestClient):
        """
        LLM 모델은 mock으로 바꿔서 테스트
        """

        response = test_client.post(
            "api/problems/predict-difficulty",
            json={"url": "https://programmers.co.kr/learn/courses/30/lessons/12921"},
        )

        assert response.json() == {
            "platform": "programmers",
            "difficulty": "NORMAL",
            "reason": "Mocked assessment: This is a normal difficulty problem.",
            "title": "소수 찾기",
            "url": "https://programmers.co.kr/learn/courses/30/lessons/12921",
        }
