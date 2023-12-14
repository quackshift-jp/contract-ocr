from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.crud import get
from backend.models.data_model import Contract
from backend.db import db

router = APIRouter()


@router.get("/get/contracts/", response_model=list[Contract])
async def get_contracts_endpoint() -> list[Contract]:
    result = get.get_contracts(db=next(db.get_db_session()))
    return result
