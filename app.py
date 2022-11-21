from flask import Flask
from flasgger import Swagger
from flask_restful import Api

# resources
from api.Classes.Joke import Joke
from api.Classes.Mathematic import Mathematic

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


# adding routes
api.add_resource(Joke, '/joke')
api.add_resource(Mathematic, '/math')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
