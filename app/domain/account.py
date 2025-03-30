from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Account:
    """
    Represents a bank account entity with basic financial operations.

    Attributes:
        account_id (int): Unique identifier for the account.
        balance (Decimal): Current balance of the account.
    """
    account_id: int
    balance: Decimal

    def deposit(self, amount: Decimal):
        """
        Deposits a specified amount into the account.

        Args:
            amount (Decimal): The amount of money to deposit.

        Raises:
            ValueError: If the deposit amount is zero or negative.
        """
        if amount <= Decimal('0'):
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: Decimal) -> bool:
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (Decimal): The amount of money to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.

        Raises:
            ValueError: If the withdrawal amount is zero or negative.
        """
        if amount <= Decimal('0'):
            raise ValueError("Withdrawal amount must be positive")
        if self.can_withdraw(amount):
            self.balance -= amount
            return True
        return False

    def can_withdraw(self, amount: Decimal) -> bool:
        """
        Checks if the account has sufficient balance to withdraw a specified amount.

        Args:
            amount (Decimal): The amount of money to check against the current balance.

        Returns:
            bool: True if there are sufficient funds, False otherwise.
        """
        return self.balance >= amount

