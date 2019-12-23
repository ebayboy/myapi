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

from resources.foo import Foo
from resources.bar import Bar
from resources.baz import Baz

app = Flask(__name__)
api = Api(app)


api.add_resource(Foo, '/Foo', '/Foo/<str:id>')
api.add_resource(Bar, 'Bar', '/Bar/<str:id>')
api.add_ressouce(Baz, 'Baz', '/Baz/<str:id>')
api.add_ressouce(User, 'User', '/User/<str:id>')

ass TodoSimple(Resource):
    def get(self, todo_id):
        if (todo_id in todos):
            return {todo_id: todos[todo_id]}
        else:
            return {}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
