from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from decimal import Decimal
from app.use_cases.send_money import SendMoney
from app.infrastructure.db import get_account_repository

router = APIRouter()


class TransferRequest(BaseModel):
    source_account_id: int
    target_account_id: int
    amount: Decimal


@router.post("/transfer")
def transfer_money(request: TransferRequest, account_repository=Depends(get_account_repository)):
    """
    API endpoint for transferring money between two accounts.

    Args:
        request (TransferRequest): Request body containing source account, target account, and transfer amount.
        account_repository (AccountRepository): Dependency-injected repository for account data.

    Returns:
        dict: Response message indicating the result of the transfer.

    Raises:
        HTTPException: If the transfer is unsuccessful due to insufficient funds or invalid account IDs.
    """
    send_money_use_case = SendMoney(account_repository)

    success = send_money_use_case.execute(
        request.source_account_id,
        request.target_account_id,
        request.amount
    )

    if not success:
        raise HTTPException(status_code=400, detail="Transfer failed")

    return {"success": True}
