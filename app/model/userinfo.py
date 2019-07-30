# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, LargeBinary, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound

from app.model import Base, User


class UserInfo(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    address = Column(String(20), nullable=False)
    dob = Column(Date, nullable=False)
    contact = Column(String(15), nullable=True)
    nationality = Column(String(50), nullable=False)
    verified = Column(Boolean, nullable=False, default=False)

    user = relationship("User", back_populates="userinfo")

    def __repr__(self):
        return "<UserInfo(adrress='%s', dob='%s')>" % (
            self.address,
            self.dob,
        )

    @classmethod
    def get_id(cls):
        return UserInfo.id

    @classmethod
    def find_by_user_id(cls, session, user_id):
        try:
            return session.query(UserInfo).filter(UserInfo.user_id == user_id).one()
        except NoResultFound:
            return None

    FIELDS = {"address": str, "dob": str, "contact": str, "nationality": str, "verified": bool}

    FIELDS.update(Base.FIELDS)
    FIELDS.update(User.FIELDS)
