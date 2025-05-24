import requests

def fetch_dependencies(package: str) -> dict:
    response = requests.get(f"https://api.tea.xyz/v1/dependencies/{package}")
    response.raise_for_status()
    return response.json()