from backend.schemas.schemas import Employee, Contract, EmployeeEvent
from datetime import datetime


def test_employee():
    employee_data = {
        "employee_id": 11111,
        "name": "山田太郎",
        "created_at": "2099-01-01 01:00:00",
    }

    actual = Employee(**employee_data)
    expected = {
        "employee_id": 11111,
        "name": "山田太郎",
        "created_at": datetime(2099, 1, 1, 1, 0),
    }
    assert actual == expected


def test_contract():
    contract_data = {
        "contract_id": 11111,
        "contractor": "サンプル株式会社",
        "created_at": "2099-01-01 01:00:00",
        "updated_at": "2099-01-01 01:00:00",
    }

    actual = Contract(**contract_data)
    expected = {
        "contract_id": 11111,
        "contractor": "サンプル株式会社",
        "created_at": datetime(2099, 1, 1, 1, 0),
        "updated_at": datetime(2099, 1, 1, 1, 0),
    }
    assert actual == expected


def test_employee_event():
    event_data = {
        "contract_id": 11111,
        "employee_id": 22222,
        "created_at": "2099-01-01 01:00:00",
        "updated_at": "2099-01-01 01:00:00",
        "event_type": "CREATED",
    }

    actual = EmployeeEvent(**event_data)
    expected = {
        "contract_id": 11111,
        "employee_id": 22222,
        "created_at": datetime(2099, 1, 1, 1, 0),
        "updated_at": datetime(2099, 1, 1, 1, 0),
        "event_type": "CREATED",
    }
    assert actual == expected
