#!/usr/bin/python3

# /****************************************************************************
# @file:user.py
# @author:ebayboy@163.com
# @date:2019-12-23 21:40
# @version 1.0
# @description: python file
# @Copyright (c)  all right reserved
# **************************************************************************/

from myapi.models import User
from manage import db

#将表映射为对象User
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=False)


#def create_user():
def create_user():
    # 创建一个新用户对象
    user = User()
    user.username = 'fuyong'
    user.password = '123'

    # 将新创建的用户添加到数据库会话中
    db.session.add(user)
    # 将数据库会话中的变动提交到数据库中, 记住, 如果不 commit, 数据库中是没有变化的.
    db.session.commit()

create_user()


def delete_user():
    # 获取用户对象
    user=User.query.filter_by(id=1).first()

    # 删除用户
    db.session.delete(user)

    # 提交数据库会话
    db.session.commit()

delete_user()



def update_user():
    # 获取用户对象
    user=User.query.filter_by(id=2).first()

    # 修改用户
    user.password='123567'

    # 提交数据库会话
    db.session.commit()

update_user()

def select_user():
    # 查询所有用户
    users_list=User.query.all()

    # 查询用户名称为 fuyong 的第一个用户, 并返回用户实例, 因为之前定义数据库的时候定义用户名称唯一, 所以数据库中用户名称为 test
    # 的应该只有一个.
    user=User.query.filter_by(username='fuyong').first()
    # or
    user=User.query.filter(User.username == 'fuyong').first()

    # 模糊查询, 查找用户名以abc 结尾的所有用户
    users_list=User.query.filter(User.username.endsWith('g')).all()

    # 查询用户名不是 fuyong 的第一个用户
    user=User.query.filter(User.username != 'fuyong').first()

if __name__ == '__main__':
    app.run(debug=True)


