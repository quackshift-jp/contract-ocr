from pydantic import BaseModel
from datetime import datetime


class Employee(BaseModel):
    employee_id: int
    name: str
    created_at: datetime


class Contract(BaseModel):
    contract_id: int
    image_link: str
    contractor: str
    created_at: datetime
    updated_at: datetime


class EmployeeEvent(BaseModel):
    contract_id: int
    employee_id: int
    created_at: datetime
    updated_at: datetime
    event_type: str
