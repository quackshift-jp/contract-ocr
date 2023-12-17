from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from backend.schemas.schemas import Contract
from datetime import datetime


def update_contract(contract_id: int, contract: str, db: Session) -> None:
    current_date = datetime.utcnow().strftime("%Y-%m-%d %H%M%S")
    sql = text(
        f"""
    update contract \
    set contractor = '{contract}', \
    updated_at = '{current_date}' \
    where contract_id = {contract_id}
    """
    )

    db.execute(sql)
    db.commit()
