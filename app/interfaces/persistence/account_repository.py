from typing import Optional
from app.domain.account import Account
from sqlalchemy.orm import Session


class AccountRepository:
    """
    Repository class for managing Account persistence.

    Attributes:
        db_session (Session): SQLAlchemy session object for database interactions.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_by_id(self, account_id: int) -> Optional[Account]:
        """
        Retrieves an account by its ID.

        Args:
            account_id (int): Unique identifier of the account to retrieve.

        Returns:
            Optional[Account]: The account object if found, otherwise None.
        """
        return self.db_session.query(Account).filter(Account.account_id == account_id).first()

    def update(self, account: Account):
        """
        Updates an account's data in the database.

        Args:
            account (Account): The account entity to update.
        """
        self.db_session.merge(account)
        self.db_session.commit()
