#!/usr/bin/python3

# /****************************************************************************
# @file:app.py
# @author:ebayboy@163.com
# @date:2019-12-23 15:46
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

from flask import Flask, Request, jsonify, got_request_exception
from flask_restful import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
import sys

#import resource
import config
from db import db
from werkzeug.exceptions import HTTPException
import common.common as cm
from common.common import Common

from resources.User import User, UserList
from resources.Constellation import Constellation, ConstellationList


def log_exception(sender, exception, **extra):
    "Log an exception to our logging framework",
    sender.logger.debug('Got exception during processing: %s', exception)


app = Flask(__name__)
app.config.from_object(config)

got_request_exception.connect(log_exception, app)

api = Api(app, catch_all_404s=True, errors=cm.errors)

# Add resources

# User
api.add_resource(User, '/User', '/User/<string:username>')
api.add_resource(UserList, '/UserList')

# Constellation
api.add_resource(
    Constellation,
    '/Constellation',
    '/Constellation/<string:name>')
api.add_resource(ConstellationList, '/ConstellationList')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
