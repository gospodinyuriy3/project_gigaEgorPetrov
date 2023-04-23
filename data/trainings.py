import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Training(SqlAlchemyBase):
    __tablename__ = 'training'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    trainer = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('users.id'))
    train = sqlalchemy.Column(sqlalchemy.String,
                            nullable=True)
    aboniment = sqlalchemy.Column(sqlalchemy.Integer,
                                  nullable=True)
    chads = sqlalchemy.Column(sqlalchemy.String,
                                      nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean,
                                    default=True)
    user = orm.relationship('User')

    def __repr__(self):
        return f'<Training> {self.tarining}'
