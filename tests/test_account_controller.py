# tests/test_account_controller.py

import pytest
from fastapi.testclient import TestClient
from decimal import Decimal
from app.main import app
from app.domain.account import Account
from app.use_cases.send_money import SendMoney
from unittest.mock import patch

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_send_money():
    with patch('app.interfaces.api.account_controller.SendMoney') as mock:
        yield mock

def test_send_money_api_success(client, mock_send_money):
    """
    Test successful API call to send money between accounts.
    """
    # Arrange
    mock_instance = mock_send_money.return_value
    mock_instance.execute.return_value = True

    # Act
    response = client.post("/accounts/transfer", json={
        "source_account_id": 1,
        "target_account_id": 2,
        "amount": "200"
    })

    # Assert
    assert response.status_code == 200
    assert response.json() == {"success": True}

def test_send_money_api_failure(client, mock_send_money):
    """
    Test API call failure due to insufficient funds or other business rule.
    """
    # Arrange
    mock_instance = mock_send_money.return_value
    mock_instance.execute.return_value = False

    # Act
    response = client.post("/accounts/transfer", json={
        "source_account_id": 1,
        "target_account_id": 2,
        "amount": "500"
    })

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Transfer failed"}
