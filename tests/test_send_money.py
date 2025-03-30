# tests/test_send_money.py

import pytest
from decimal import Decimal
from unittest.mock import MagicMock
from app.domain.account import Account
from app.use_cases.send_money import SendMoney

@pytest.fixture
def mock_account_repository():
    """
    Fixture providing a mocked AccountRepository instance.
    """
    return MagicMock()

@pytest.fixture
def send_money_use_case(mock_account_repository):
    """
    Fixture providing an instance of the SendMoney use case with a mocked repository.
    """
    return SendMoney(account_repository=mock_account_repository)

def test_send_money_success(send_money_use_case, mock_account_repository):
    """
    Test successful money transfer between two accounts.

    Verifies that:
    - The transfer is successful.
    - The balances of source and target accounts are updated correctly.
    """
    # Arrange
    source_account = Account(account_id=1, balance=Decimal('500'))
    target_account = Account(account_id=2, balance=Decimal('300'))

    mock_account_repository.find_by_id.side_effect = [source_account, target_account]

    # Act
    result = send_money_use_case.execute(1, 2, Decimal('200'))

    # Assert
    assert result is True
    assert source_account.balance == Decimal('300')
    assert target_account.balance == Decimal('500')

def test_send_money_insufficient_funds(send_money_use_case, mock_account_repository):
    """
    Test unsuccessful money transfer due to insufficient funds in the source account.

    Verifies that:
    - The transfer fails.
    - The balances of both accounts remain unchanged.
    """
    # Arrange
    source_account = Account(account_id=1, balance=Decimal('100'))
    target_account = Account(account_id=2, balance=Decimal('300'))

    mock_account_repository.find_by_id.side_effect = [source_account, target_account]

    # Act
    result = send_money_use_case.execute(1, 2, Decimal('200'))

    # Assert
    assert result is False
    assert source_account.balance == Decimal('100')  # unchanged
    assert target_account.balance == Decimal('300')  # unchanged
