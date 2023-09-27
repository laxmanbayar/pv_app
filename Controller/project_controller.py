
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey,insert,MetaData,Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from DataBase.common_models import Project,User
from DataBase.DB_config import DB_config_class
from Variables import var
#from DataBase.project_specific_model import Estimation,Surface_Area
from DataBase import project_specific_model


engine=DB_config_class.engine
session=DB_config_class.session
Base=DB_config_class.Base


class ProjectController:
    
    def __init__(self,project_id=None):
        #Instance Level Variables
        self.project_id=project_id
        self.engine=DB_config_class.engine
        self.session=DB_config_class.session
        self.Base=declarative_base()
        #self.MetaData=MetaData()
 
       
        
    def create_project_output_tables(self):
        
        self.estimation_table_name="estimation"+"_"+self.project_id
        self.surfaceArea_table_name="surfaceArea"+"_"+self.project_id
        
        class Estimation(self.Base):
            __tablename__= self.estimation_table_name
            id=Column(Integer)
            item=Column(String(100))
            item_name=Column(String(100),primary_key=True)
            wt=Column(String(50))
            material=Column(String(100))

        class Surface_Area(self.Base) :
            __tablename__= self.surfaceArea_table_name
            id=Column(Integer)
            item=Column(String(100))
            item_name=Column(String(100),primary_key=True)
            #wt=Column(String(50))
            surface_area=Column(String(100))
                 
        var.Estimation_Table=Estimation
        var.SurfaceArea_Table=Surface_Area
        try:        
            self.Base.metadata.create_all(self.engine,checkfirst=True)
        except:
            self.session.rollback()    
        #return self.Estimation_Table,self.SurfaceArea_Table

        
    def add_update_item(self,item, item_name, wt,material):
        # Adding New Data
        # new_item = {'id': None, 'item': item,'item_name':item_name,'wt':wt,'material':material}
        # row = self.Estimation_Table.insert().values(new_item)
        # session.execute(row)
        # session.commit()
         #check if item exist in table
        existing_item=None
        try:
            existing_item=self.session.query(var.Estimation_Table).filter_by(item_name=item_name).one()
        except Exception as e:
            self.session.rollback()
        
        #if item exist then update otherwise add item.
        if existing_item:
            existing_item.wt=wt
            existing_item.material=material
            self.session.merge(existing_item)
            
        else:
            insert_item=var.Estimation_Table(item=item,item_name=item_name,wt=wt,material=material)
            self.session.add(insert_item)
        self.session.commit()
    
    def add_update_surface_area(self,item, item_name,surface_area):
        existing_item=None
        try:
            existing_item=self.session.query(var.SurfaceArea_Table).filter_by(item_name=item_name).one()
        except SQLAlchemyError as e:
            self.session.rollback()
        
        #if item exist then update otherwise add item.
        if existing_item:
            #existing_item.wt=wt
            existing_item.surface_area=surface_area
            self.session.merge(existing_item)
            
        else:
            insert_item=var.SurfaceArea_Table(item=item,item_name=item_name,surface_area=surface_area)
            self.session.add(insert_item)
        self.session.commit()     
                    


    def read_estimation_table(self):
        try:
            data = self.session.query(var.Estimation_Table).all()
            # Get the column names
            column_names = var.Estimation_Table.__table__.columns.keys()
        
            return data,column_names
                
        except SQLAlchemyError as e:
            self.session.rollback()
        # end try
  
    def read_surface_area_table(self):
        try:
            data = self.session.query(var.SurfaceArea_Table).all()
            # Get the column names
            column_names = var.SurfaceArea_Table.__table__.columns.keys()
        
            return data,column_names
            
        except SQLAlchemyError as e:
            self.session.rollback()
        # end try  

def create_new_project(proj_id,proj_name,project_note,user,status="Active"):
    try:
        new_project = Project(project_id=proj_id, project_name=proj_name, project_note=project_note,user_staffNo=user, status=status) 
        # Add and commit the changes   
        session.add(new_project)
        session.commit()        
    except SQLAlchemyError as e:
        session.rollback()
       
    
def Get_all_existing_projects():
    query = session.query(Project.project_id)
    project_ids = query.all()
    project_ids_list=[project_id[0] for project_id in project_ids]
    project_ids_list.insert(0,None)
    return project_ids_list

def get_current_project_details(project_id):
    try:
        project_detail=session.query(Project).filter_by(project_id=project_id).one()
        return project_detail
    except Exception as e:
        session.rollback()
            
    