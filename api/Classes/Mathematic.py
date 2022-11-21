from .Abstract import SquadMethods
from flask_restful import Resource
from flask import request
from .Process import Process


class Mathematic(
    SquadMethods,
    Resource
):

    def __init__(
        self,
        instance_of: Process = Process
    ):
        self.instance_of = instance_of()

    def get(self):
        """
        Example endpoint returning a result number depending on params passed
        if params contains numbers or number this return a specific operation
        ---
        parameters:
          - in: query
            type: integer
            name: number
            required: true
          - in: query
            type: list
            name: numbers
            required: true
        responses:
          200:
            description: result number
          400:
            description: missing or invalid parameters
        """
        self.instance_of.event_process(
            request.args, ["numbers", "number"])

        if request.args.get("number"):
            number = self.instance_of.add_one(request.args)
        else:
            number = (
                self.instance_of.mcm(request.args.to_dict(flat=False)))
        return {
            "result": number
        }, 200
