from datetime import datetime

from sqlalchemy import (Column, Integer, String, BigInteger,
                        ForeignKey, Float, Date, DateTime, Boolean)
from sqlalchemy.orm import relationship
from db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_tg_id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime)

    def __repr__(self):
        return f'<Users(id={self.id}, user_name={self.user_name}, first_name={self.first_name}, last_name={self.last_name}, user_tg_id={self.user_tg_id}, created_at={self.created_at})>'

    class Config:
        orm_mode = True


class Channels(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_id = Column(Integer, ForeignKey('users.id'))
    channel_name = Column(String(50))
    channel_tg_id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime)

    admin = relationship("Users", lazy="subquery", back_populates="channels")

    def __repr__(self):
        return f'<Channels(id={self.id}, admin_id={self.admin_id}, channel_name={self.channel_name}, channel_tg_id={self.channel_tg_id}, created_at={self.created_at})>'

    class Config:
        orm_mode = True


class Advirtisment(Base):
    __tablename__ = 'ads'

    ad_id = Column(Integer, primary_key=True, autoincrement=True)
    ad_name = Column(String(20))
    ad_text = Column(String)
    cost_for_1000 = Column(Float)
    ad_chanel_id = Column(BigInteger)
    advertiser_user_id = Column(Integer, ForeignKey('users.user_tg_id'))
    region = Column(String)
    theme = Column(String)
    creation_date = Column(DateTime, default=datetime.now)
    shows = Column(BigInteger, default=0)
    status = Column(String)

    advertiser = relationship("User", back_populates="ads", lazy="subquery")

    class Config:
        orm_mode = True


class AdPlacements(Base):
    __tablename__ = 'ad_placements'

    placement_id = Column(Integer, primary_key=True, autoincrement=True)
    ad_id = Column(Integer, ForeignKey('advertisements.ad_id'))
    channel_id = Column(Integer, ForeignKey('channels.channel_id'))
    placement_date = Column(DateTime, default=datetime.now)

    # Определение связи с моделью Advertisements (один-ко-многим)
    ad = relationship("Advertisements", back_populates="placements")

    # Определение связи с моделью Channels (один-ко-многим)
    channel = relationship("Channels", back_populates="placements")

    class Config:
        orm_mode = True

# class Payment(Base):
#     __tablename__ = "payment_history"
#
#     id = Column(BigInteger, autoincrement=True, primary_key=True)

