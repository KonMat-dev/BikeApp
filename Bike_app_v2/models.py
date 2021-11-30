import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy_utils import EmailType

from Bike_app_v2.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    description = Column(String, index=True)
    hashed_password = Column(String, index=True)
    email = Column(EmailType)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, index=True, default=True)
