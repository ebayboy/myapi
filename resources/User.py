
#from flask_jwt import jwt_required
from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse
import json

from models.UserModel import UserModel

# check for email


def email(email_str):
    """ return True if email_str is a valid email """
    if valid_email(email):
        return True
    else:
        raise ValidationError("{} is not a valid email")

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='The user\'s username',
)
post_parser.add_argument(
    'password', dest='password',
    type=str, location='form',
    help='The user\'s passoword',
)
post_parser.add_argument(
    'email', dest='email',
    type=email, location='form',
    help='The user\'s email',
)
post_parser.add_argument(
    'user_priority', dest='user_priority',
    type=int, location='form',
    default=1, choices=range(5), help='The user\'s priority',
)

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'sub': fields.String,
    'uuid': fields.String,
    'extra': fields.String,
    'date_created': fields.DateTime,
    'tel': fields.String,
    'user_priority': fields.Integer
}

class User(Resource):
    @marshal_with(user_fields)
    def post(self, username):
        if UserModel.find_by_name(username):
            return {
                'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()
        user = UserModel(username, **data)

        try:
            user.create_user()
        except BaseException:
            return {"message": "An error occurred inserting the item."}, 500

        return user.json(), 201

    @marshal_with(user_fields)
    def get(self, username):
        user = UserModel.find_by_name(username)
        if user: 
            return user;
        else:
            return {"message": "Not found"}, 404


class UserList(Resource):
    @marshal_with(user_fields)
    def get(self): 
        return UserModel.query.all();



