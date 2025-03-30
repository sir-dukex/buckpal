from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from app.interfaces.persistence.account_repository import AccountRepository

DATABASE_URL = "sqlite:///./test.db"  # For demonstration purposes

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db_session() -> Session:
    """
    Context manager for managing SQLAlchemy database sessions.

    Yields:
        Session: A database session.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# Dependency-injected function to provide AccountRepository
def get_account_repository():
    """
    Dependency provider for AccountRepository instances.

    Returns:
        AccountRepository: An instance of the AccountRepository with an active database session.
    """
    with get_db_session() as session:
        yield AccountRepository(session)
