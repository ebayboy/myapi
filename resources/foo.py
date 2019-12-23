#!/usr/bin/python3

#/****************************************************************************
#@file:foo.py 
#@author:ebayboy@163.com 
#@date:2019-12-23 15:46 
#@version 1.0  
#@description: python file 
#@Copyright (c)  all right reserved 
#**************************************************************************/

from flask import Flask,Request
from flask_restful import Api, Resource

class Foo(Resource):
    def get(self):
        pass
    def post(self):
        pass

