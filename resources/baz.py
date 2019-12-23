#!/usr/bin/python3

#/****************************************************************************
#@file:bar.py 
#@author:ebayboy@163.com 
#@date:2019-12-23 15:46 
#@version 1.0  
#@description: python file 
#@Copyright (c)  all right reserved 
#**************************************************************************/

from flask import Flask,Request
from flask_restful import Api, Resource

class Baz(Resource):
    def get(self):
        pass
    def post(self):
        pass

