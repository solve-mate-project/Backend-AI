from fastapi import APIRouter, HTTPException, Depends
from dependency_injector.wiring import inject, Provide

from src.adapter.dto.problem_dto import (
    ProblemPredictDifficultyRequest,
    ProblemPredictDifficultyResponse,
)
from src.application.usecases.predict_problem_difficulty import (
    PredictProblemDifficultyUseCase,
)
from src.containers import Container

router = APIRouter(tags=["Problem"])


@router.post(
    "/problems/predict-difficulty",
    response_model=ProblemPredictDifficultyResponse,
)
@inject
async def predict_difficulty(
    body: ProblemPredictDifficultyRequest,
    predict_difficulty_uc: PredictProblemDifficultyUseCase = Depends(
        Provide[Container.predict_difficulty_uc]
    ),
) -> ProblemPredictDifficultyResponse:
    """문제 URL을 받아 난이도를 예측합니다."""

    # 유스케이스 실행
    problem = await predict_difficulty_uc.execute(str(body.url))

    if not problem:
        raise HTTPException(
            status_code=404, detail="문제를 찾을 수 없거나 지원하지 않는 URL입니다."
        )

    # 응답 생성
    return ProblemPredictDifficultyResponse(
        platform=problem.platform,
        difficulty=problem.difficulty,
        reason=problem.difficulty_explanation,
        title=problem.title,
        url=problem.url,
    )
