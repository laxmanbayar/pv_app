
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from DataBase.common_models import Project,User
from DataBase.DB_config import DB_config_class
from Variables import var
from DataBase.project_specific_model import Estimation,Surface_Area
from DataBase import project_specific_model


engine=DB_config_class.engine
session=DB_config_class.session
Base=DB_config_class.Base

# #Base= declarative_base()

# estimation_table_name="estimation"+"_"+project_id
# surfaceArea_table_name="surfaceArea"+"_"+project_id


# class Estimation(Base):
#     __tablename__= estimation_table_name
#     id=Column(Integer)
#     item=Column(String(100))
#     item_name=Column(String(100),primary_key=True)
#     wt=Column(String(50))
#     material=Column(String(100))
    
# class Surface_Area(Base) :
#     __tablename__= surfaceArea_table_name
#     id=Column(Integer)
#     item=Column(String(100))
#     item_name=Column(String(100),primary_key=True)
#     #wt=Column(String(50))
#     surface_area=Column(String(100))  
    
        
# def create_project_op_tables():
#     Base.metadata.create_all(engine) 

  # Create a new declarative base
base = declarative_base()
class EstimationTable(base, Estimation):
    def __init__(self,project_id):
        __tablename__ = "estimation_"+project_id

class SurfaceAreaTable(base,Surface_Area):
    def __init__(self,project_id):
         __tablename__ = "surface_area_"+project_id
            
class ProjectController:
    def __init__(self):
        self.engine=DB_config_class.engine
        self.session=DB_config_class.session
        #self.EstimationTable=None
        #self.SurfaceAreaTable=None
                
        
    def create_project_output_tables(self,project_id):
        class EstimationTable(base, Estimation):
            def __init__(self,project_id):
                __tablename__ = "estimation_"+project_id
                
        class SurfaceAreaTable(base,Surface_Area):
            def __init__(self,project_id):
             __tablename__ = "surface_area_"+project_id        
                
        self.EstimationTable=EstimationTable(project_id)
        self.SurfaceAreaTable=SurfaceAreaTable(project_id)

     
        # Create the table
        base.metadata.create_all(self.engine)
     
    def get_project_output_table(self):        
        self.EstimationTable=EstimationTable(var.project_id)
        self.SurfaceAreaTable=SurfaceAreaTable(var.project_id)
        return self.EstimationTable,self.SurfaceAreaTable
           
    def add_or_update_material(self, item, item_name, wt,material):
        insert_item = self.EstimationTable(item=item,item_name=item_name,wt=wt,material=material)
        self.session.add(insert_item)
        self.session.commit()    
    def add_or_update_surface_area(item,item_name,surface_area):
        insert_item=Surface_Area(item=item,item_name=item_name,surface_area=surface_area)
        session.add(insert_item)
        session.commit() 
               
    def read_estimation_table(self):
        try:
            data = session.query(self.EstimationTable).all()
            # Get the column names
            column_names = self.EstimationTable.__table__.columns.keys()
        
            return data,column_names
                
        except SQLAlchemyError as e:
            pass
        # end try
  
    def read_surface_area_table(self):
        try:
            data = session.query(self.SurfaceAreaTable).all()
            # Get the column names
            column_names = self.SurfaceAreaTable.__table__.columns.keys()
        
            return data,column_names
            
        except SQLAlchemyError as e:
            pass
        # end try  
            
        # project_specific_model.PROJECT_ID=projectid
        # project_specific_model.estimation_table_name+=projectid
        # project_specific_model.surfaceArea_table_name+=projectid
        # Estimation.__tablename__=project_specific_model.estimation_table_name
        # Surface_Area.__tablename__=project_specific_model.surfaceArea_table_name
        #Create_Project_OP_Tables(projectid)
    # estimation=Estimation() 
        # Estimation.__tablename__="estimation_"+projectid
        # Surface_Area.__tablename__="surfaceArea_"+projectid
        # Estimation.metadata.create_all(engine)
        # Surface_Area.metadata.create_all(engine)   
        
#create_project_op_tables()

def create_new_project(proj_id,proj_name,user,status="Active"):
    try:
        new_project = Project(project_id=proj_id, project_name=proj_name, user_staffNo=user, status=status) 
        # Add and commit the changes   
        session.add(new_project)
        session.commit()        
    except SQLAlchemyError as e:
        pass
    # end try
   
def create_project_output_tables(projectid):
    # project_specific_model.PROJECT_ID=projectid
    # project_specific_model.estimation_table_name+=projectid
    # project_specific_model.surfaceArea_table_name+=projectid
    # Estimation.__tablename__=project_specific_model.estimation_table_name
    # Surface_Area.__tablename__=project_specific_model.surfaceArea_table_name
    #Create_Project_OP_Tables(projectid)
   # estimation=Estimation() 
    Estimation.__tablename__="estimation_"+projectid
    Surface_Area.__tablename__="surfaceArea_"+projectid
    Estimation.metadata.create_all(engine)
    Surface_Area.metadata.create_all(engine)   
    
def add_or_update_material(item,item_name,wt,material):
    #check if item exist in table
    existing_item=None
    try:
        existing_item=session.query(Estimation).filter_by(item_name=item_name).one()
    except SQLAlchemyError as e:
        pass
    
    #if item exist then update otherwise add item.
    if existing_item:
        existing_item.wt=wt
        existing_item.material=material
        session.merge(existing_item)
        
    else:
        insert_item=Estimation(item=item,item_name=item_name,wt=wt,material=material)
        session.add(insert_item)
    session.commit()
   
def add_or_update_surface_area(item,item_name,surface_area):
    existing_item=None
    try:
        existing_item=session.query(Surface_Area).filter_by(item_name=item_name).one()
    except SQLAlchemyError as e:
        pass
    
    #if item exist then update otherwise add item.
    if existing_item:
        #existing_item.wt=wt
        existing_item.surface_area=surface_area
        session.merge(existing_item)
        
    else:
        insert_item=Surface_Area(item=item,item_name=item_name,surface_area=surface_area)
        session.add(insert_item)
    session.commit()     
    
def read_estimation_table():
  try:
    data = session.query(Estimation).all()
     # Get the column names
    column_names = Estimation.__table__.columns.keys()
   
    return data,column_names
         
  except SQLAlchemyError as e:
    raise e
  # end try
  
def read_surface_area_table():
    try:
        data = session.query(Surface_Area).all()
        # Get the column names
        column_names = Surface_Area.__table__.columns.keys()
    
        return data,column_names
         
    except SQLAlchemyError as e:
        raise e
    # end try  
      