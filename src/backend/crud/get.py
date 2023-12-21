from typing import Union
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import HTTPException

from backend.schemas.schemas import Contract


def get_contracts(db: Session) -> list[Contract]:
    sql = text("select * from contract;")
    result = db.execute(sql).all()
    if result is None:
        raise HTTPException(status_code=404, detail="Table not found")
    contracts = [Contract(**row._asdict()) for row in result]
    return contracts


def get_specific_contract(
    column_name: str, column_value: str, db: Session
) -> Union[None, Contract]:
    sql = text(
        f"""
        SELECT * FROM contract WHERE {column_name} = '{column_value}';
    """
    )
    result = db.execute(sql).first()
    if result is None:
        return None  # Return None if no data is found
    return Contract(**result._asdict())
