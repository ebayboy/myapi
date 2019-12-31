#!/usr/bin/python3

# /****************************************************************************
# @file:db_setting.py
# @author:ebayboy@163.com
# @date:2019-12-23 21:37
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'Xiang010'
HOST = 'www.codedayday.com'
PORT = '3306'
DATABASE = 'codedayday'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

