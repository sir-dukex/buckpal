from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AccountDBModel(Base):
    """
    ORM model representing the 'accounts' table in the database.
    """
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, index=True)
    balance = Column(Numeric(15, 2), nullable=False)
