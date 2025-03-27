from fastapi.testclient import TestClient


class TestPredictDifficultyEP:
    def test_predict_difficulty(self, test_client: TestClient):
        """
        TODO: mock으로 바꿔서 테스트 필요
        """

        response = test_client.post(
            "api/problems/predict-difficulty",
            json={"url": "https://programmers.co.kr/learn/courses/30/lessons/12921"},
        )
