#!/usr/bin/python3

# /****************************************************************************
# @file:user.py
# @author:ebayboy@163.com
# @date:2019-12-23 21:40
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

from db import db

# 将表映射为对象User
class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), primary_key=True, nullable=False)
    password = db.Column(db.String(45), nullable=True)
    email =  db.Column(db.String(45), nullable=True)
    sub =  db.Column(db.String(45), nullable=True)
    uuid =  db.Column(db.String(45), nullable=True)
    extra =  db.Column(db.String(45), nullable=True)
    date_created =  db.Column(db.DateTime, nullable=True)
    user_priority = db.Column(db.Integer, nullable=True)
    tel =  db.Column(db.String(45), nullable=True)
    timestamp =  db.Column(db.DateTime, nullable=True)

    def create_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def update_user(self):
        db.session.add(user)
        db.session.commit()

    def select_user():
        users_list = UserModel.query.all()

    @classmethod
    def find_by_name(self, username):
        return db.session.query(UserModel.username).filter_by(username=username).first()

if __name__ == '__main__':
    app.run(debug=True)
