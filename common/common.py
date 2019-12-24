#!/usr/bin/python3

# /****************************************************************************
# @file:common/common.py
# @author:ebayboy@163.com
# @date:2019-12-24 15:46
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

from flask import jsonify
from werkzeug.exceptions import HTTPException

class AlreadyExistsError(HTTPException):
    pass

class ResourceDoesNotExistError(HTTPException):
    pass

errors = {
    'AlreadyExistsError': {
        'message': "It is already exist.",
        'status': 409
    },
    'ResourceDoesNotExistError': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want."
    }
}

class Common:
    def returnTrueJson(self, data, message="success"):
        print("data:", data)
        ret=jsonify({
            "status": 1,
            "data": data,
            "message": message
        })
        print("ret:", ret)
        return ret

    def returnFalseJson(self, data=None, message="failed"):
        return jsonify({
            "status": 0,
            "data": data,
            "message": message
        })
