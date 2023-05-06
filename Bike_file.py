from sqlalchemy import Column, Integer, String
from database import Base


class Bike(Base):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    cc = Column(Integer)
    color = Column(String(20))
    price = Column(Integer)
