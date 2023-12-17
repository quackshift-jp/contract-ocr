import requests


def read_contract_endpoint(endpoint: str) -> list[dict[str, any]]:
    response = requests.get(endpoint)
    if response.status_code == 200:
        json_data = response.json()
        return json_data


def insert_contract_endpoint(endpoint: str, contractor: str) -> list[dict[str, any]]:
    response = requests.post(f"{endpoint}?contractor={contractor}")
    if response.status_code == 200:
        return response.json()


def update_contract_endpoint(
    contract_id: int,
    contractor: str,
    endpoint: str,
) -> dict[str, str]:
    response = requests.put(
        f"{endpoint}{contract_id}?contract_id={contract_id}&contractor={contractor}"
    )
    if response.status_code == 200:
        return response.json()
