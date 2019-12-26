#!/usr/bin/python3

# /****************************************************************************
# @file:constellation.py
# @author:ebayboy@163.com
# @date:2019-12-23 21:40
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

from db import db
import json
from sqlalchemy.orm import class_mapper
from datetime import datetime
from flask_restful import fields, marshal_with


# 将表映射为对象Constellation
class ConstellationModel(db.Model):
    __tablename__ = 'constellation'

    name = db.Column(db.String(45), primary_key=True, nullable=False)

    date = db.Column(db.Integer, nullable=True)
    datetime = db.Column(db.String(45), nullable=True)
    all = db.Column(db.String(45), nullable=True)
    color = db.Column(db.String(45), nullable=True)
    health = db.Column(db.String(45), nullable=True)
    love = db.Column(db.String(45), nullable=True)
    money = db.Column(db.String(45), nullable=True)
    number = db.Column(db.Integer, nullable=True)
    QFriend = db.Column(db.String(255), nullable=True)
    summary = db.Column(db.String(255), nullable=True)
    work = db.Column(db.String(45), nullable=True)

    def create_constellation(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except BaseException:
            db.session.rollback()
            db.session.flush()
            return None

    def update_constellation(self):
        try:
            db.session.commit()
            return self
        except BaseException:
            db.session.rollback()
            db.session.flush()
            return None


    def delete_constellation(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self
        except BaseException:
            db.session.rollback()
            db.session.flush()
            return None

    def select_constellation():
        constellations_list = ConstellationModel.query.all()

    @classmethod
    def find_by_name(self, name):
        return ConstellationModel.query.filter_by(name=name).first()


if __name__ == '__main__':
    app.run(debug=True)
