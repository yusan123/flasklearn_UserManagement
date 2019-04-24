# _*_coding:utf-8_*_
# author：qq823947488
# date：2019/4/24 20:15

from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(),primary_key=True,autoincrement=True)
    username=Column(String(),nullable=False)
    password=Column(String(),nullable=False)

    def __init__(self,username,password):
        self.username=username
        self.password=password