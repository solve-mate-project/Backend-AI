import logging
from contextlib import contextmanager
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.util.preloaded import orm

logger = logging.getLogger(__name__)


DBBase = declarative_base()


def create_db_engine(db_user: str, db_pwd: str, db_host: str, db_name: str):
    return create_engine(
        f"mysql+pymysql://{db_user}:{db_pwd}@{db_host}:3306/{db_name}",
        pool_pre_ping=True,
        echo=False,
    )


class Database:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        )

    @contextmanager
    def session(self):
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
