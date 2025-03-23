from fastapi import FastAPI

from src.adapter.api.problem_router import router as problem_router
from src.containers import Container


def create_app() -> FastAPI:
    """애플리케이션 팩토리"""

    # FastAPI 앱 생성
    _app = FastAPI(title="Coding Problem Analyzer API")

    # 의존성 컨테이너 설정
    _container = Container()
    _app.state.container = _container
    _app.include_router(problem_router, prefix="/api")
    return _app


app = create_app()
