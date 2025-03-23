from pydantic import BaseModel, HttpUrl, Field


class ProblemPredictDifficultyRequest(BaseModel):
    url: HttpUrl


class ProblemPredictDifficultyResponse(BaseModel):
    platform: str = Field(title="플랫폼")
    difficulty: str = Field(title="난이도")
    reason: str = Field(title="난이도 설명")
    title: str = Field(title="문제 제목")
    url: str = Field(title="문제 URL")
