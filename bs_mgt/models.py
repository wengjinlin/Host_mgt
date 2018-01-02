from django.db import models

# Create your models here.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Host(Base):
    # 主机表
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True)
    ip = Column(String(64), unique=True)
    port = Column(Integer)
    os = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id'))
    group_id = Column(Integer, ForeignKey('host_group.id'))

    def __repr__(self):
        return self.hostname


class Group(Base):
    # 主机分组表
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(64), unique=True)

    hosts = relationship('Host', backref='host_group')

    def __repr__(self):
        return self.groupname


class User(Base):
    # 用户表
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))
    nickname = Column(String(32))

    hosts = relationship('Host', backref='user')

    def __repr__(self):
        return self.username
