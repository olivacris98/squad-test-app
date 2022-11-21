from abc import ABC, abstractmethod


class SquadMethods(ABC):

    """
        this abstract is responsible for get method that will be use in
        squad apis
    """

    @abstractmethod
    def get(self) -> dict:
        pass


class JokeMethods(SquadMethods):
    """
        this abstract class is responsible for all method that must content
        joke test
    """

    def __init__(self):
        pass

    @abstractmethod
    def post(self) -> dict:
        pass

    @abstractmethod
    def put(self) -> dict:
        pass

    @abstractmethod
    def delete(self) -> dict:
        pass

    def response(status_code, data):
        return
