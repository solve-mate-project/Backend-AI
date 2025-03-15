from pydantic import BaseModel, HttpUrl


class ProblemPredictDifficultyRequest(BaseModel):
    url: HttpUrl


class ProblemPredictDifficultyResponse(BaseModel):
    platform: str
    difficulty: str
    reason: str
    title: str
    url: str
