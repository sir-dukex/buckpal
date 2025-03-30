# tests/test_account_repository.py

import pytest
from decimal import Decimal
from app.infrastructure.db_models import Base, AccountDBModel
from app.interfaces.persistence.account_repository import AccountRepository
from app.infrastructure.db import get_db_session, create_engine, DATABASE_URL
from app.domain.account import Account

# テスト前後にテーブルを再作成するfixture
@pytest.fixture(scope="function")
def test_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def account_repository(test_db):
    with get_db_session() as session:  # 正しい使い方に修正
        repo = AccountRepository(session)
        yield repo

def test_account_repository_create_and_find(account_repository):
    """
    Test creating an account and retrieving it from the database.
    """
    new_account = Account(account_id=1, balance=Decimal('500'))
    account_repository.update(new_account)

    fetched_account = account_repository.find_by_id(1)
    assert fetched_account is not None
    assert fetched_account.account_id == new_account.account_id
    assert fetched_account.balance == new_account.balance

def test_account_repository_update(account_repository):
    """
    Test updating an existing account's balance.
    """
    account = Account(account_id=2, balance=Decimal('300'))
    account_repository.update(account)

    account.balance = Decimal('600')
    account_repository.update(account)

    fetched_account = account_repository.find_by_id(2)
    assert fetched_account.balance == Decimal('600')

