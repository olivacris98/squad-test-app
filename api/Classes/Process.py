from ..Utils.helpers import (
    JOKE_ENDPOINTS, PARAMETERS, MAX_LEN_PARAMS,
    INVALID_PARAM, PUT_PARAMS)
from flask import abort


class Process:

    def __init__(self):
        pass

    @staticmethod
    def random_url() -> str:
        """get random endpoint"""
        import random
        return random.choice(list(JOKE_ENDPOINTS.values()))

    @classmethod
    def get_joke_process(self, query_params) -> bool:
        """process get endpoint"""

        # validate len of request
        self.max_len_request(query_params)

        # validate params
        self.get_parameters(value=list(query_params.values())[0])
        return self.get_endpoint_by_name(param=list(query_params.values())[0])

    @ staticmethod
    def get_joke(joke: dict) -> dict:
        """get joke from"""
        return (
            joke.get('joke')
            if joke.get("joke")
            else joke.get("value"))

    @ staticmethod
    def get_endpoint_by_name(param: str) -> str:
        return JOKE_ENDPOINTS[param]

    @staticmethod
    def max_len_request(
        request_data: dict,
        max_len: int = MAX_LEN_PARAMS
    ) -> bool:
        """validate max len of request
            raises errors if the condition is not satisfied
        """
        if len(request_data) > max_len:
            abort(400, INVALID_PARAM)
        return True

    @classmethod
    def event_process(
        self,
        payload: dict,
        param: list[str]
    ) -> bool:

        """process event"""

        # validate if contains information
        self.validate_request(payload)

        # validate len of request
        self.max_len_request(payload)

        # validate if contains param
        self.get_parameters(value=list(payload.keys())[0], parameters=param)
        return True

    @staticmethod
    def get_parameters(
        value: str,
        parameters: list = PARAMETERS
    ) -> bool:

        if value not in parameters:
            abort(400, INVALID_PARAM)
        return True

    @staticmethod
    def alpha_space(param: str):
        """Checks param is alphanumeric containing spaces or middle dashes"""
        from re import fullmatch as re_fullmatch
        _str = r"^[A-Za-z0-9_À-ÿ0-9][A-Za-z0-9_À-ÿ0-9\.\-\_ ]{0,255}[a-zA-Z0-9]$"

        if not re_fullmatch(_str, param.rstrip()):
            abort(400, INVALID_PARAM)

    @classmethod
    def post_event(
        self,
        payload: dict,
        param: list[str],
    ) -> bool:
        """validate post event"""
        self.event_process(payload, param)
        print("1")

        # validate string data
        self.alpha_space(payload.get(param))
        print("2")

    @staticmethod
    def mcm(kwargs) -> int:
        """get mcm of list numbers
        """
        import math
        numbers_str = kwargs.get('numbers')
        return math.lcm(*[int(x) for x in numbers_str])

    @staticmethod
    def add_one(payload) -> int:
        """get int and sum + 1
        """
        return int(payload.get('number')) + 1

    @staticmethod
    def validate_request(payload) -> bool:
        if not payload:
            abort(400, INVALID_PARAM)
        return True

    @classmethod
    def put_event(
        self,
        payload: dict,
    ) -> bool:
        """validate post event"""

        self.validate_request(payload)

        # validate params
        check = any(
            item in list(payload.keys())
            for item in PUT_PARAMS)

        if not check:
            abort(400, INVALID_PARAM)
