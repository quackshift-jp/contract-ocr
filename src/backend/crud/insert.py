from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from datetime import datetime
from backend.schemas.schemas import Contract


def insert_contract(contractor: str, db: Session) -> list[Contract]:
    current_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    sql = text(
        f"""
    insert into contract (contractor, created_at, updated_at) values \
    ('{contractor}', '{current_date}', '{current_date}')
    """
    )
    db.execute(sql)
    db.commit()
    sql_2 = text("select * from contract order by contract_id desc")
    return db.execute(sql_2).first()
