from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values,load_dotenv
import os
import pandas as pd

try:
   from DataBase.DB_config import DB_config_class
except Exception as e:
   from DB_config import DB_config_class

#from DB_config import DB_config


# DATABASE_URL=DB_config_class.db_url

#    # comment:    
# print(DATABASE_URL)
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()
engine=DB_config_class.engine
session= DB_config_class.session

Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = "user"

    staffNo = Column(String(50), primary_key=True)
    name = Column(String(50))
    pwd = Column(String(50))
    role=Column(String(50))
    status=Column(String(50))
    projects = relationship("Project", back_populates="user")

# Define Project model
class Project(Base):
    __tablename__ = "project"

    project_id = Column(String(50), primary_key=True)
    project_name = Column(String(50))
    user_staffNo = Column(String(50), ForeignKey("user.staffNo")) 
    status = Column(String(50))
    user = relationship("User", back_populates="projects", foreign_keys=[user_staffNo])
    
class Material(Base):
   __tablename__="material"
   #id=Column(Integer)
   material = Column(String(100),primary_key=True)  
   


# Create tables
Base.metadata.create_all(engine)



# Insert new user and project
try:
   new_user = User(staffNo="6209254", name="Laxman B", pwd="6209254",role="admin",status="enabled")
   new_project = Project(project_id="P1", project_name="Sample Project", user_staffNo="6209254", status="Active") 
   # Add and commit the changes
   session.add(new_user)
   session.add(new_project)
   session.commit()
   print(new_user.name)
except Exception as e:
   #raise e
  #print(e)
  session.rollback()
# end try



# Query user's projects
user = session.query(User).filter_by(staffNo="6209254").first()
#user=session.query(User).filter(staffNo=='6209254')
print(user.projects)
for project in user.projects:
    print("Project:", project.project_name)

# Close the session
session.close()
























# from peewee import *
# #from peewee import PostgresqlDatabase
# from dotenv import dotenv_values
# import os
# try:
#    from DataBase.db_creation import PV_DB_creation
# except Exception as e:
#    from db_creation import PV_DB_creation 


# #Get DB context for Sqlite or MYSQL depending upon mode variable in env
# config=dotenv_values('.env')
# mode=config['MODE']
# db_name=config['DB_NAME']
# new_db_creation=PV_DB_creation()
# new_db_creation.create_db() #This will create  "PV_BOM" Database

# #Get DB contex
# if(mode=='prod'):
#    db_config={
#    'host':config['DB_HOST'],
#    'port':int(config['DB_PORT']),
#    'user':config['DB_USER'],
#    'password':config['DB_PASSWORD']
   
#    }
   
#    db=MySQLDatabase(database=db_name,**db_config)
# elif(mode=='dev'):
#    db=SqliteDatabase(db_name+'.db')   

# # #Initial Schemas for various tables
# # # class User (Model):
# # #    staffNo=CharField(primary_key=True,)
# # #    name=CharField()
# # #    pwd=CharField(null=False)
# # #    role=CharField(default='user')
# # #    status=CharField(default='disabled')
   
# # #    class Meta:
# # #       database=db
# # #       db_table='User'


# # # class Project (Model):
# # #    project_id=CharField()
# # #    project_name=IntegerField()
# # #    staffNo=ForeignKeyField(User)
# # #    status=CharField(default='wip')
# # #    class Meta:
# # #       database=db
# # #       db_table='Project'
      

# # from peewee import *

# # #db = MySQLDatabase('my_database')

# # class User(Model):
# #   staffNo = CharField(primary_key=True)
# #   name = CharField()
# #   email = CharField()
# #   phoneNo = CharField()
# #   designation = CharField()
# #   class Meta:
# #      database=db
# #      db_table='user'

# # class Project(Model):
# #   projectId = IntegerField(primary_key=True)
# #   name = CharField()
# #   description = CharField()
# #   startDate = DateTimeField()
# #   endDate = DateTimeField()
# #   staffNo = ForeignKeyField(User,backref='projecs')
# #   class Meta:
# #       database=db
# #       db_table='project'

# # with db:
# #     db.create_tables([User, Project]) 
    
    
# # # db.connect()
# # # db.create_tables([User,Project])  


# # # Insert a new user
# # new_user = User(staffNo='12345', name='John Doe', email='johndoe@example.com', phoneNo='123-456-7890', designation='Software Engineer')
# # new_user.save()

# # # Insert a new project
# # new_project = Project(name='Project X', description='This is a new project.', startDate='2023-08-17', endDate='2023-09-17', staffNo=new_user)
# # new_project.save()      
      


# # if __name__=='__main__':
# #    abcd = PV_DB_creation()




