import requests


def request_read_contract_endpoint(endpoint: str) -> list[dict[str, any]]:
    response = requests.get(endpoint)
    if response.status_code == 200:
        json_data = response.json()
        return json_data


def request_insert_contract_endpoint(
    endpoint: str, contractor: str
) -> list[dict[str, any]]:
    response = requests.post(f"{endpoint}?contractor={contractor}")
    if response.status_code == 200:
        json_data = response.json()
        return json_data
