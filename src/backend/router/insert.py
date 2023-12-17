from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from backend.crud import insert
from backend.db import db

router = APIRouter()


@router.post("/insert/contracts", response_model=dict[str, str])
async def insert_contracts_endpoint(
    contractor: str,
    db: Session = Depends(db.get_db_session),
) -> dict[str, str]:
    try:
        insert.insert_contract(contractor, db=db)
        return {"message": f"insert success: contractor={contractor}"}
    except Exception as e:
        HTTPException(status_code=400, detail=str(e))
