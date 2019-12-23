from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse


#check for email
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
    'email', dest='email',
    type=email, location='form',
    required=True, help='The user\'s email',
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
    'roles': fields.String,
    'extra': fields.String,
    'date_created': fields.DateTime,
    'tel': fields.String,
    'user_priority': fields.Integer
}

class User(restful.Resource):

    @marshal_with(user_fields)
    def post(self):
        args = post_parser.parse_args()
        user = create_user(args.username, args.email, args.user_priority)
        return user

    @marshal_with(user_fields)
    def get(self, id):
        args = get_parser.parse_args()
        user = fetch_user(id)
        return user



