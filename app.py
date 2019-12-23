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

from myapi.resources.foo import Foo
from myapi.resources.bar import Bar
from myapi.resources.baz import Baz

app = Flask(__name__)
api = Api(app)


api.add_resource(Foo, '/Foo', '/Foo/<str:id>')
api.add_resource(Bar, 'Bar', '/Bar/<str:id>')
api.add_ressouce(Baz, 'Baz', '/Baz/<str:id>')


if __name__ == '__main__':
    app.run(debug=True)
