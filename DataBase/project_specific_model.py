# from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from DataBase.common_models import Project,User
# from DataBase.DB_config import DB_config_class
# #from Variables.var import project_id


# # engine=DB_config_class.engine
# # session=DB_config_class.session
# # Base=DB_config_class.Base

# #Base= declarative_base()
# # PROJECT_ID=""
# # estimation_table_name="estimation"+"_"+PROJECT_ID
# # surfaceArea_table_name="surfaceArea"+"_"+PROJECT_ID

# class Estimation():
#     #__tablename__= estimation_table_name
#     id=Column(Integer)
#     item=Column(String(100))
#     item_name=Column(String(100),primary_key=True)
#     wt=Column(String(50))
#     material=Column(String(100))

# class Surface_Area() :
#     #__tablename__= surfaceArea_table_name
#     id=Column(Integer)
#     item=Column(String(100))
#     item_name=Column(String(100),primary_key=True)
#     #wt=Column(String(50))
#     surface_area=Column(String(100))     
        
# # def Create_Project_OP_Tables(projectid):
#     pass
#     # class Estimation(Base):
#     #     __tablename__= "estimation_"+projectid
#     #     id=Column(Integer)
#     #     item=Column(String(100))
#     #     item_name=Column(String(100),primary_key=True)
#     #     wt=Column(String(50))
#     #     material=Column(String(100))
    
#     # class Surface_Area(Base) :
#     #     __tablename__= "surfaceArea_"+projectid
#     #     id=Column(Integer)
#     #     item=Column(String(100))
#     #     item_name=Column(String(100),primary_key=True)
#     #     #wt=Column(String(50))
#     #     surface_area=Column(String(100))  
#     # Estimation.__tablename__=estimation_table_name+projectid
#     # Surface_Area.__tablename__=surfaceArea_table_name+projectid
#     # Base.metadata.create_all(engine) 