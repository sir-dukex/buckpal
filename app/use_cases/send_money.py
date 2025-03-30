from decimal import Decimal
from typing import Optional
from app.domain.account import Account
# from app.interfaces.persistence.account_repository import AccountRepository
from app.domain.ports.account_repository_port import AccountRepositoryPort


class SendMoney:
    """
    Use case for handling money transfers between two accounts.

    Attributes:
        account_repository (AccountRepositoryPort): Repository interface for account data.
    """

    def __init__(self, account_repository: AccountRepositoryPort):
        self.account_repository = account_repository

    def execute(self, source_account_id: int, target_account_id: int, amount: Decimal) -> bool:
        """
        Executes a money transfer from the source account to the target account.

        Args:
            source_account_id (int): ID of the account to transfer money from.
            target_account_id (int): ID of the account to transfer money to.
            amount (Decimal): The amount of money to transfer.

        Returns:
            bool: True if the transfer was successful, False otherwise.
        """
        source_account: Optional[Account] = self.account_repository.find_by_id(source_account_id)
        target_account: Optional[Account] = self.account_repository.find_by_id(target_account_id)

        if source_account is None or target_account is None:
            return False

        if not source_account.withdraw(amount):
            return False

        target_account.deposit(amount)

        self.account_repository.update(source_account)
        self.account_repository.update(target_account)

        return True
