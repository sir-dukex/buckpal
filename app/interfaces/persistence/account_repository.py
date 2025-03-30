from typing import Optional
from decimal import Decimal
from sqlalchemy.orm import Session
from app.domain.account import Account
from app.infrastructure.db_models import AccountDBModel
from app.domain.ports.account_repository_port import AccountRepositoryPort

class AccountRepository(AccountRepositoryPort):
    """
    Repository class for managing persistence operations for Account entities.

    This class handles all database interactions related to accounts, including
    retrieval, creation, and updating account data.

    Attributes:
        db_session (Session): SQLAlchemy session object for database interactions.
    """

    def __init__(self, db_session: Session):
        """
        Initializes the AccountRepository with a database session.

        Args:
            db_session (Session): SQLAlchemy session instance.
        """
        self.db_session = db_session

    def find_by_id(self, account_id: int) -> Optional[Account]:
        """
        Retrieves an account by its unique identifier from the database.

        Args:
            account_id (int): Unique identifier of the account.

        Returns:
            Optional[Account]: The corresponding Account domain entity if found; otherwise, None.
        """
        account_db = (
            self.db_session.query(AccountDBModel)
            .filter(AccountDBModel.account_id == account_id)
            .first()
        )

        if account_db:
            # Convert ORM model to domain model
            return Account(
                account_id=account_db.account_id,
                balance=Decimal(account_db.balance)
            )
        return None

    def update(self, account: Account):
        """
        Updates the specified account's information in the database. If the account does not exist, creates a new entry.

        Args:
            account (Account): The Account domain entity to update or create.
        """
        account_db = (
            self.db_session.query(AccountDBModel)
            .filter(AccountDBModel.account_id == account.account_id)
            .first()
        )

        if account_db:
            # Update existing record
            account_db.balance = account.balance
        else:
            # Create a new record
            account_db = AccountDBModel(
                account_id=account.account_id,
                balance=account.balance
            )
            self.db_session.add(account_db)

        self.db_session.commit()

