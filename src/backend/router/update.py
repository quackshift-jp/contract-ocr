from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from backend.schemas.schemas import Contract
from backend.db import db
from backend.crud import update

router = APIRouter()


@router.put("/update/contracts/{contracts_id}", response_model=dict[str, str])
async def update_contract_endpoint(
    contract_id: int, contractor: str, db: Session = Depends(db.get_db_session)
):
    try:
        update.update_contract(contract_id, contractor, db=db)
        return {"message": f"contract_id {contract_id} is updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
