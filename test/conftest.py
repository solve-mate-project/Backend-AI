import pytest
from unittest.mock import AsyncMock
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from dependency_injector.providers import Singleton

from src.domain.entities.problem import DifficultyLevel
from src.infrastructure.database.database_connection import DBBase, Database
from src.infrastructure.services.LLMDifficultyPredictor import LLMDifficultyPredictor
from main import app


@pytest.fixture
def in_memory_sqlite_db():
    # SQLite 메모리 데이터베이스 엔진 생성
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    # 데이터베이스 테이블 생성
    DBBase.metadata.create_all(engine)
    return engine


@pytest.fixture
def session_factory(in_memory_sqlite_db):
    # 세션 팩토리 생성
    return sessionmaker(autocommit=False, autoflush=False, bind=in_memory_sqlite_db)


@pytest.fixture
def mock_difficulty_predictor():
    # AsyncMock을 사용하여 비동기 메서드 모킹
    mock_predictor = AsyncMock(spec=LLMDifficultyPredictor)

    # predict_difficulty 메서드의 반환값 설정
    mock_predictor.predict_difficulty.return_value = (
        DifficultyLevel.NORMAL,
        "Mocked assessment: This is a normal difficulty problem.",
    )

    # model_name 속성 설정
    mock_predictor.model_name = "mocked_model"

    return mock_predictor


@pytest.fixture
def test_client(in_memory_sqlite_db, mock_difficulty_predictor):
    app.state.container.db_schema.override(Singleton(Database, engine=in_memory_sqlite_db))  # type: ignore
    app.state.container.difficulty_predictor.override(mock_difficulty_predictor)

    return TestClient(app)
