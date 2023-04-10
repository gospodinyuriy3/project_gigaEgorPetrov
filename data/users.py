import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String,
                                 nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer,
                            nullable=True)
    height = sqlalchemy.Column(sqlalchemy.Integer,
                               nullable=True)
    weight = sqlalchemy.Column(sqlalchemy.Integer,
                               nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String,
                                   nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              unique=True,
                              nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String,
                                        nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now(),
                                      nullable=True)