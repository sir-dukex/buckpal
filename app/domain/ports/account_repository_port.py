from abc import ABC, abstractmethod
from typing import Optional
from app.domain.account import Account


class AccountRepositoryPort(ABC):
    """
    Abstract repository interface for account data operations.
    This is the contract that the domain/use-case layer depends on.
    """

    @abstractmethod
    def find_by_id(self, account_id: int) -> Optional[Account]:
        pass

    @abstractmethod
    def update(self, account: Account):
        pass
