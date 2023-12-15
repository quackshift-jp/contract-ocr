from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException
from backend.schemas.schemas import Contract


def get_contracts(db: Session) -> list[Contract]:
    sql = text("select * from contract;")
    result = db.execute(sql).all()
    if result is None:
        raise HTTPException(status_code=404, detail="Table not found")
    return result
