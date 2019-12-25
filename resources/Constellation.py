
# from flask_jwt import jwt_required
from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse, abort, marshal

from models.ConstellationModel import ConstellationModel
from common.common import *
import sys

# check for email

class Constellation(Resource):
    def get(self, name):
        user = ConstellationModel.find_by_name(name)
        if user:
            return Common.returnTrueJson(Common, marshal(user, user_fields))

        raise ResourceDoesNotExistError(
            "name '{}' not exist!".format(name))

class ConstellationList(Resource):
    def get(self):
        userlist = ConstellationModel.query.all()
        if userlist:
            return Common.returnTrueJson(
                Common, marshal(userlist, user_fields))

        raise ResourceDoesNotExistError("Not found!")
