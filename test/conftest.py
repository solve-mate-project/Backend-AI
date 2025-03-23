import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from dependency_injector.providers import (
    Singleton,
)
from src.infrastructure.database.database_connection import DBBase, Database
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
def test_client(in_memory_sqlite_db):
    app.state.container.db_schema.override(Singleton(Database, engine=in_memory_sqlite_db))  # type: ignore
    return TestClient(app)
