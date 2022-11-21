"""The tests to run in this project.
To run the tests type,
"""

import unittest
import math


BASE_URL = "http://localhost:5000/test/text_base.py"
HEADERS = {'Accept': 'application/json'}


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
        import requests
        response = requests.get(end_point, headers=HEADERS)
        return response.json() if response.status_code == 200 else {}

    def post_data():
        pass


class TestSquad(unittest.TestCase):

    def test_mcm(self):
        list_of_numbers = ["2", "4", "5"]
        self.assertTrue(type(list_of_numbers) is list)
        calculate = math.lcm(*[int(x) for x in list_of_numbers])
        self.assertEqual(type(calculate), int)

    def test_add_one(self) -> int:
        """get int and sum + 1
        """
        params = {"number": "3"}
        self.assertEqual(int(params.get('number')) + 1, 4)

    def test_random_joke(self):

        JOKE_ENDPOINTS = {
            "Chuck": "https://api.chucknorris.io/jokes/random",
            "Dad": "https://icanhazdadjoke.com/"
        }

        import random
        url_end = random.choice(list(JOKE_ENDPOINTS.values()))

        print(url_end)
        request = Requester().get_request(url_end)
        self.assertEqual(type(request), dict)

if __name__ == '__main__':
    unittest.main()