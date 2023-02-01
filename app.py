from flask import Flask
from flask_restful import Resource, Api, reqparse
from marshmallow import Schema, fields


app = Flask('main')
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('name', location='args')
parser.add_argument('description', location='args')
parser.add_argument('severity', location='args')


class TaskSchema(Schema):
    name = fields.String()
    description = fields.String()
    severity = fields.Integer()


class TaskResource(Resource):
    def get(self):
        schema = TaskSchema()
        args = parser.parse_args()
        return schema.dump(args)


api.add_resource(TaskResource, '/')


app.run(debug=True)
