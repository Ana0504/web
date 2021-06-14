from sqlalchemy import Column, ForeignKey, Integer, String, Text ,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

"""
Модуль с описанием ORM-моделей базы данных
"""

# Подключение объекта для управления БД
from labapp import db

class Login(db.Model):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class ContactRequest(db.Model):
    __tablename__ = 'contactrequest'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255))
    email = Column(String(255))
    reqtype = Column(String(255))
    reqtext = Column(Text(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

