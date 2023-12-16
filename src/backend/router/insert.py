from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.crud import insert
from backend.schemas.schemas import Contract
from backend.db import db

router = APIRouter()


@router.post("/insert/contracts", response_model=Contract)
async def insert_contracts_endpoint(
    contractor: str,
    db: Session = Depends(db.get_db_session),
) -> list[Contract]:
    result = insert.insert_contract(contractor, db=db)
    return result
