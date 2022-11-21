import requests
from ..Utils.helpers import HEADERS


class Requester:

    def __init__(self):
        pass

    @classmethod
    def get_request(self, end_point: str) -> dict:
        """make a get http request
        Args:
          end_point: (str)
        Returns:
          processed response (dict)
        """
        response = requests.get(end_point, headers=HEADERS)
        return response.json() if response.status_code == 200 else {}

    def post_data():
        pass
