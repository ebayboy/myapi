
# from flask_jwt import jwt_required
from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse, abort, marshal

from models.UserModel import UserModel
from common.common import *

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
    def post(self):
        data = post_parser.parse_args()

        if UserModel.find_by_name(data.username):
            raise AlreadyExistsError(
                "An item with name '{}' already exists.".format(
                    data.username))

        user = UserModel(**data)
        try:
            user.create_user()
        except BaseException:
            raise InternelServerError("An error occurred inserting the item. '{}'".
                                      format(data.username))

        return Common.returnTrueJson(Common, marshal(user, user_fields))

    def get(self, username):
        user = UserModel.find_by_name(username)
        if user:
            return Common.returnTrueJson(Common, marshal(user, user_fields))

        raise ResourceDoesNotExistError(
            "username '{}' not exist!".format(username))


class UserList(Resource):
    def get(self):
        userlist = UserModel.query.all()
        if userlist:
            return Common.returnTrueJson(
                Common, marshal(userlist, user_fields))

        raise ResourceDoesNotExistError("Not found!")
