from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine=create_engine('mysql://root:dny800@localhost/customer',echo=True)
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()
class Student(Base):
   __table__='student'
   id=Column(Integer, primary_key = True)
   name=Column(String(50))
   age=Column(Integer)
   grade=Column(String(50))
Base.metadata.create_all(engine)
