from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_contracts(db: Session) -> list[tuple]:
    sql = text("select * from contract;")
    result = db.execute(sql).all()
    return result
