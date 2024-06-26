from sqlalchemy.ext.asyncio import create_async_engine
from core.config import settings
from sqlalchemy.orm import sessionmaker


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False
        )


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo
)
