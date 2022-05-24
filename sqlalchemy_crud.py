from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine=create_engine('mysql+pymysql://root:dny800@localhost/sqlalchemy',echo=True)
Base=declarative_base()
class Student(Base):
   __tablename__='student'
   id=Column(Integer, primary_key = True)
   name=Column(String(50))
   age=Column(Integer)
   grade=Column(String(50))
Base.metadata.create_all(engine)

#add data to student table

Session=sessionmaker(bind=engine)
session=Session()
stud1=Student(id=7,name='suresh',age=30,grade='C')
session.add(stud1)
session.commit()

