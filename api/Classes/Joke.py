from flask_restful import Resource
from flask import request
from .Abstract import JokeMethods
from flasgger import swag_from
from .Process import Process
from .Requester import Requester
from ..Databases.db import Session
from ..Models.Joke import JokeModel


class Joke(Resource, JokeMethods):
    """
    This class is responsible Joke methods
    """

    def __init__(self, instance_of: Process = Process):
        self.instance_of = instance_of()

    def get(self):
        """
        Example endpoint returning a joke depends on params sended
        if params contains Dad or Chunk this return a specific joke selected
        otherwise return a random joke
        ---
        parameters:
          - in: query
            type: string
            enum: ['Chunk', 'Dad']
            required: false
        responses:
          200:
            description: jokes obtained successfully
          400:
            description: missing or invalid parameters
        """
        if request.args:
            endpoint = self.instance_of.get_joke_process(request.args)
        else:
            # get random api and process
            endpoint = self.instance_of.random_url()

        # process json response
        return {
            "statusCode": 200,
            "joke": self.instance_of.get_joke(
                Requester().get_request(endpoint)),
        }, 200

    def put(self):
        """
        Example endpoint returning a joke updated
        ---
        parameters:
          - in: body
            name: joke
            description: joke relational description
            schema:
                properties:
                squad_test:
                    type: object
                    properties:
                    joke:
                        type: string
                        example: new joke
                    number:
                        type: integer
                        example: 4
        responses:
          200:
            description: joke updated successfully
          400:
            description: missing or invalid parameters
        """
        payload = request.get_json()
        self.instance_of.put_event(payload)

        session = Session()

        joke = (
            session.query(JokeModel)
            .filter_by(number=payload.get("number"))
            .first()
        )
        joke.joke = payload.get("joke")
        session.add(joke)
        session.commit()

        message = "Joke updated successfully"

        return {"message": message}, 200

    def delete(self):
        """
        Example endpoint returning a joke deleted
        ---
        parameters:
          - in: query
            type: integer
            name: number
            required: true
        responses:
          200:
            description: jokes deleted successfully
          400:
            description: missing or invalid parameters
        """
        self.instance_of.event_process(request.args, ["number"])

        session = Session()
        joke = (
            session.query(JokeModel)
            .filter_by(number=request.args.get("number"))
            .first()
        )

        session.delete(joke)
        session.commit()
        message = "Joke deleted successfully"

        return {"message": message}, 200

    def post(self):
        """
        Example endpoint returning a joke created
        ---
        parameters:
          - in: body
            name: joke
            description: joke relational description
            schema:
                properties:
                squad_test:
                    type: object
                    properties:
                    joke:
                        type: string
                        example: new joke
                    example:
                    joke: this a new joke
        responses:
          200:
            description: joke saved successfully
          400:
            description: missing or invalid parameters
        """
        payload = request.get_json()

        # validate process
        self.instance_of.post_event(payload, param="joke")

        session = Session()
        joke = JokeModel(joke=payload.get("joke"))
        session.add(joke)
        session.commit()

        return {
            "message": "¡Joke saved successfully!",
            "number": joke.number}, 201
