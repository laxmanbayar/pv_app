
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey,insert,MetaData,Table,and_,func
from sqlalchemy.sql import cast
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from DataBase.common_models import Project,User,Elbow,Skirt_Base,WN_FLG,Long_WN_FLG,Saddle,Saddle_Dim,Vessel,Side_downcomer,Center_offcenter_downcomer
from DataBase.DB_config import DB_config_class
from Variables import var
#from DataBase.project_specific_model import Estimation,Surface_Area
from DataBase import project_specific_model


engine=DB_config_class.engine
session=DB_config_class.session
Base=DB_config_class.Base


#Add update delete Itens in estimation and Surface are atable for a existing project
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



#Other FUnctionality read/write 
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
            
def Get_Elbow_Details(nps,schedule):
    try:
        elbow_detail=session.query(Elbow).filter(and_ (Elbow.NPS==nps , Elbow.SCHEDULE==schedule)).all()
        return elbow_detail[0]
   
    except Exception as e:
        session.rollback()       

def Get_gusset_detail(bolt_size):
    try:
        #As data may not be sorted in the table
        results = session.query(Skirt_Base).filter(cast(Skirt_Base.Bolt, Integer) >= bolt_size).all()
        #sort the result based on Bolt columns(as data in the database table may not be sorted)
        sorted_result = sorted(results, key=lambda x: int(x.Bolt))
        return sorted_result[0]
    except Exception as e:
        print(e)
        session.rollback()  
    # end try
    
def Get_WL_FLG_detail(classs,nps):
    try:
        #As data may not be sorted in the table
        results = session.query(WN_FLG).filter(and_(WN_FLG.nps==nps , WN_FLG.classs==classs)).all()
        #sort the result based on Bolt columns(as data in the database table may not be sorted)
        #sorted_result = sorted(results, key=lambda x: int(x.Bolt))
        return results[0]
    except Exception as e:
        print(e)
        session.rollback()  
    # end try    
def Get_Shell_ODs_from_Saddle_Data():
    try:
        shell_ODs = session.query(Saddle.D).all()        
        shell_ODs_list=[int(shell_OD[0]) for shell_OD in shell_ODs]  
        shell_ODs_list.sort()      
        return shell_ODs_list      
    except Exception as e:
        print(e)
        session.rollback() 
        
def Get_Saddle_Data(shell_OD):
    try: 
        #Get Nearest OD Value from the database and then return that row having nearest value    
        req_od = session.query(Saddle.D).order_by(func.abs(cast(Saddle.D,Integer) - shell_OD)).limit(1).scalar()
        result = session.query(Saddle).filter(Saddle.D==req_od).all()
        return result[0]
    except Exception as e:
        print(e)
        session.rollback()          

def Get_Saddle_Dim_Data(saddle_type):
    try:       
        results = session.query(Saddle_Dim).filter(Saddle_Dim.Type==saddle_type).all()       
        return results[0]
    except Exception as e:
        print(e)
        session.rollback() 
        
def Get_Vessel_Data(Vessel_OD):
    try:      
         #Get Nearest OD Value from the database and then return that row having nearest value  
        req_od = session.query(Vessel.OD) \
                        .order_by(func.abs(cast(Vessel.OD,Integer) - Vessel_OD)) \
                        .limit(1) \
                        .scalar()
        results = session.query(Vessel).filter(Vessel.OD == req_od).all()                    
        return results[0]
    except Exception as e:
        print(e)
        session.rollback()                      
        
def Get_DownComer_Data(Vessel_Dia,is_side):
    try: 
        if(is_side):     
            #Get Nearest OD Value from the database and then return that row having nearest value  
            req_od = session.query(Side_downcomer.Vessel_ID_upto) \
                            .order_by(func.abs(cast(Side_downcomer.Vessel_ID_upto,Integer) - Vessel_Dia)) \
                            .limit(1) \
                            .scalar()
            results = session.query(Side_downcomer).filter(Side_downcomer.Vessel_ID_upto == req_od).all()                    
            return results[0]
        else:
            req_od = session.query(Center_offcenter_downcomer.Vessel_ID_upto) \
                            .order_by(func.abs(cast(Center_offcenter_downcomer.Vessel_ID_upto,Integer) - Vessel_Dia)) \
                            .limit(1) \
                            .scalar()
            results = session.query(Center_offcenter_downcomer).filter(Center_offcenter_downcomer.Vessel_ID_upto == req_od).all()                    
            return results[0]
            
    except Exception as e:
        print(e)
        session.rollback()         