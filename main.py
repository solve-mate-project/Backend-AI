from fastapi import FastAPI

from src.adapter.api.problem_router import router as problem_router
from src.containers import Container


def create_app() -> FastAPI:
    """애플리케이션 팩토리"""

    # FastAPI 앱 생성
    app = FastAPI(title="Coding Problem Analyzer API")

    # 의존성 컨테이너 설정
    container = Container()
    app.container = container

    # 라우터 등록
    app.include_router(problem_router, prefix="/api")

    # 의존성 주입 설정
    container.wire(modules=["src.adapter.api.problem_router"])

    return app


app = create_app()
