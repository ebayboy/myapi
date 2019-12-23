#!/usr/bin/python3

# /****************************************************************************
# @file:app.py
# @author:ebayboy@163.com
# @date:2019-12-23 15:46
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

from flask import Flask, Request
from flask_restful import Api, Resource, fields

#import resource
from resources.foo import Foo
from resources.bar import Bar
from resources.baz import Baz
from resources.r_user import User

app = Flask(__name__)
api = Api(app)

#add resource
api.add_resource(Foo, '/Foo', '/Foo/<string:id>')
api.add_resource(Bar, '/Bar', '/Bar/<string:id>')
api.add_resource(Baz, '/Baz', '/Baz/<string:id>')
api.add_resource(User, '/User', '/User/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
