from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.crud import get
from backend.schemas.schemas import Contract
from backend.db import db

router = APIRouter()


@router.get("/get/contracts/", response_model=list[Contract])
async def get_contracts_endpoint(
    db: Session = Depends(db.get_db_session),
) -> list[Contract]:
    result = get.get_contracts(db=db)
    return result
