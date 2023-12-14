# customer.py
from sqlalchemy import Column, Integer, String
from base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))

    def __init__(self, id, name, age, email):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
