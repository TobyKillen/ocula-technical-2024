import requests


class HttpClient:
    def __init__(self) -> None:
        pass

    def get(self, url: str) -> dict:
        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            raise e
    