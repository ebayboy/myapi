
# from flask_jwt import jwt_required
from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse, abort, marshal

from models.ConstellationModel import ConstellationModel
from common.common import *
import sys

# check for email

constellation_fields = {
    'name': fields.String,
    'date': fields.Integer,
    'datetime': fields.String,
    'all': fields.String,
    'color': fields.String,
    'health': fields.String,
    'love': fields.String,
    'money': fields.String,
    'number': fields.Integer,
    'QFriend': fields.String,
    'summary': fields.String,
    'work': fields.String
}

class Constellation(Resource):
    def post(self):
        dic_filter=marshal(request.form, constellation_fields)

        if ConstellationModel.find_by_name(format(dic_filter['name'])):
            raise AlreadyExistsError( "An item with name '{}' already exists.".format(dic_filter['name']))

        constellation = ConstellationModel(**dic_filter)
        if constellation.create_constellation() is None:
            raise InternelServerError("An error occurred inserting the item. '{}'".
                                      format(dic_filter['name']))
        return Common.returnTrueJson(Common, marshal(
            constellation, constellation_fields))

    def get(self, name):
        constellation = ConstellationModel.find_by_name(name)
        if constellation:
            return Common.returnTrueJson(Common, marshal(
                constellation, constellation_fields))

        raise ResourceDoesNotExistError(
            "name '{}' not exist!".format(name))


class ConstellationList(Resource):
    def get(self):
        constellationlist = ConstellationModel.query.all()
        if constellationlist:
            return Common.returnTrueJson(
                Common, marshal(constellationlist, constellation_fields))

        raise ResourceDoesNotExistError("Not found!")

