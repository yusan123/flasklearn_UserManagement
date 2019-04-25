# _*_coding:utf-8_*_
# author：qq823947488
# date：2019/4/24 20:20

from model.user import User

from utils.db_util import get_session

session = get_session()


def list_all():
    return session.query(User).all()


def get_by_id(id):
    return session.query(User).filter(User.id == id).one()


def login(username, passowrd):
    return session.query(User.username == username and User.password == passowrd).first()


def add(username,password):
    session.add(User(username,password))
    session.commit()


def update_password(id,password):
    user = get_by_id(id)
    user.password=password
    session.commit()
def delete(id):
    user = get_by_id(id)
    session.delete(user)
    session.commit()

if __name__ == '__main__':
    zs = User("zs","123")
    add(zs)