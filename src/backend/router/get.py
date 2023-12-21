from typing import Union
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
    contracts = get.get_contracts(db=db)
    return contracts


@router.get("/get/contract", response_model=Union[None, Contract])
async def get_specific_contract_endpoint(
    column_name: str,
    column_value: str,
    db: Session = Depends(db.get_db_session),
) -> Contract:
    contracts = get.get_specific_contract(column_name, column_value, db=db)
    print("タイプの出力")
    print(type(contracts))
    print(contracts)
    return contracts
