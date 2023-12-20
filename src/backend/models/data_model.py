from sqlalchemy import DateTime, Integer, Column, String
from sqlalchemy.sql import func


class Contract:
    __tablename__ = "contract"
    contract_id = Column("contract_id", Integer, primary_key=True, autoincrement=True)
    contractor = Column("contractor", String(150), nullable=False)
    created_at = Column("created_at", DateTime, nullable=False)
    updated_at = Column(
        "updated_at", DateTime, nullable=False, server_default=func.now()
    )
