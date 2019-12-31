
# from flask_jwt import jwt_required
from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse, abort, marshal

from models.UserModel import UserModel
from common.common import *
import sys

# check for email

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='The user\'s username',
)
post_parser.add_argument(
    'password', dest='password',
    type=str, location='form',
    help='The user\'s password',
)
post_parser.add_argument(
    'email', dest='email',
    type=str, location='form',
    help='The user\'s email',
)
post_parser.add_argument(
    'sub', dest='sub',
    type=str, location='form'
)
post_parser.add_argument(
    'uuid', dest='uuid',
    type=str, location='form'
)
post_parser.add_argument(
    'extra', dest='extra',
    type=str, location='form'
)
post_parser.add_argument(
    'date_created', dest='date_created',
    location='form'
)
post_parser.add_argument(
    'tel', dest='tel',
    type=str, location='form'
)

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
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
        if user.create_user() is None:
            raise InternelServerError("An error occurred inserting the item. '{}'".
                                      format(data.username))
        return Common.returnTrueJson(Common, marshal(user, user_fields))

    def get(self, username):
        user = UserModel.find_by_name(username)
        if user:
            return Common.returnTrueJson(Common, marshal(user, user_fields))

        raise ResourceDoesNotExistError(
            "username '{}' not exist!".format(username))

    def delete(self, username):
        user = UserModel.find_by_name(username)
        if user is None:
            raise ResourceDoesNotExistError(
                "username '{}' not exist!".format(username))

        if user.delete_user() is None:
            raise InternelServerError("An error occurred deleting...")

        return Common.returnTrueJson(Common, marshal(user, user_fields))

    def put(self):
        data = post_parser.parse_args()
        if UserModel.find_by_name(data.username) is None:
            raise ResourceDoesNotExistError(
                "username '{}' not exist!".format(username))

        user = UserModel(**data)
        if user.update_user() is None:
            raise InternelServerError("An error occurred update_user the item. '{}'".
                                      format(data.username))
        return Common.returnTrueJson(Common, marshal(user, user_fields))


class UserList(Resource):
    def get(self):
        userlist = UserModel.query.all()
        if userlist:
            return Common.returnTrueJson(
                Common, marshal(userlist, user_fields))

        raise ResourceDoesNotExistError("Not found!")
