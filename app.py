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
from resources.foo import Foo
from resources.bar import Bar
from resources.baz import Baz

from resources.User import User
from resources.User import UserList
from werkzeug.exceptions import HTTPException

import common.common as cm
from common.common import Common

app = Flask(__name__)
app.config.from_object(config)

got_request_exception.connect(log_exception, app)

api = Api(app, catch_all_404s=True, errors=cm.errors)

# add resource
"""
api.add_resource(Foo, '/Foo', '/Foo/<string:id>')
api.add_resource(Bar, '/Bar', '/Bar/<string:id>')
api.add_resource(Baz, '/Baz', '/Baz/<string:id>')
"""

api.add_resource(User, '/User', '/User/<string:username>')
api.add_resource(UserList, '/UserList')


def log_exception(sender, exception, **extra):
    "Log an exception to our logging framework",
    sender.logger.debug('Got exception during processing: %s', exception)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
