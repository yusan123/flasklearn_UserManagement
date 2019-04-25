# _*_coding:utf-8_*_
# author：qq823947488
# date：2019/4/24 20:25

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setting import *


def get_session():
    engine = create_engine('mysql+pymysql://%s:%s@%s:%d/%s?charset=%s' %(user,passwd,host,port,db,charset))
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    return session

if __name__ == '__main__':
    session = get_session()
    print(session.execute('select 1 '))