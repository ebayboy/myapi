#!/usr/bin/python3

# /****************************************************************************
# @file:db_manage.py
# @author:ebayboy@163.com
# @date:2019-12-23 21:38
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

from flask import Flask, request, json, Response
from flask_sqlalchemy import SQLAlchemy
import uuid

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    db.create_all()
