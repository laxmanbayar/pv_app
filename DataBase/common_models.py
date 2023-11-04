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





engine=DB_config_class.engine
session= DB_config_class.session

Base = declarative_base()



class Center_offcenter_downcomer(Base):
    __tablename__ = "center_offcenter_downcomer"
  
    id=Column(Integer,primary_key=True)
    Vessel_ID_upto=Column(String(50))
    Bolting_Bar_Width=Column(String(50))
    Bolting_Bar_Thick=Column(String(50))
    Support_Ring_Width=Column(String(50))
    Support_Ring_Thkick=Column(String(50))
   

class Elbow(Base):
    __tablename__ = "elbow"
  
    id=Column(Integer,primary_key=True)
    NPS=Column(String(50))
    SCHEDULE=Column(String(50))
    THK=Column(String(50))
    NOZL_OD=Column(String(50))
    WtPerMtr=Column(String(50))
    Wt=Column(String(50))
    Ht=Column(String(50))
    Bore=Column(String(50))
   

class Internal_flange(Base):
    __tablename__ = "internal_flange"
  
    id=Column(Integer,primary_key=True)
    NPS=Column(String(50))
    OD=Column(String(50))
    Bolt_No=Column(String(50))
    Thickness_CS=Column(String(50))
    Thickness_SS=Column(String(50))

class Leg_support(Base):
    __tablename__ = "leg_support"
  
    id=Column(Integer,primary_key=True)
    Leg_Lg=Column(String(50))
    Vessel_OD=Column(String(50))
    Size_of_Angle=Column(String(50))
    Wt_Of_Angle_per_mtr=Column(String(50))
    Base_Plate_Size=Column(String(50))
    No_of_Legs=Column(String(50))
    Max_Allowable_Load_of_Vessel=Column(String(50))
    

class Material_composition(Base):
    __tablename__ = "material_composition"
  
    id=Column(Integer,primary_key=True)
    Pipe=Column(String(50))
    Weld_Fittings=Column(String(50))
    Screwed_and_Socket_Fittings=Column(String(50))
    Flanges=Column(String(50))
    Valves=Column(String(50))
   
   
class Nozle_projection(Base):
    __tablename__ = "nozle_projection"
  
    id=Column(Integer,primary_key=True)
    NPS=Column(String(50))
    CLASS=Column(String(50))
    PROJECTION=Column(String(50))
   
   
   
class Pad_wd(Base):
    __tablename__ = "pad_wd"
  
    id=Column(Integer,primary_key=True)
    NPS=Column(String(50))
    eff85=Column(String(50))
    eff100=Column(String(50))
   

class Pipe1(Base):
    __tablename__ = "pipe1"
  
    id=Column(Integer,primary_key=True)
    A=Column(String(50))
    B=Column(String(50))
    C=Column(String(50))
    Pipe_Size=Column(String(50))
    Z=Column(String(50))
    R1=Column(String(50))
    R2=Column(String(50))
    r=Column(String(50))
    t=Column(String(50))
    Ang_Wt=Column(String(50))



class Pipe2(Base):
    __tablename__ = "pipe2"
  
    id=Column(Integer,primary_key=True)
    CLASS=Column(String(50))
    NPS=Column(String(50))
    Pipe=Column(String(50))
    B=Column(String(50))
   

class Side_downcomer(Base):
    __tablename__ = "side_downcomer"
  
    id=Column(Integer,primary_key=True)
    Vessel_ID_upto=Column(String(50))
    Bolting_Bar_Width=Column(String(50))
    Bolting_Bar_Thick=Column(String(50))
    Support_Ring_Width=Column(String(50))
    Support_Ring_Thkick=Column(String(50))


class Skirt_Base(Base):
    __tablename__ = "skirt_base"
  
    id=Column(Integer,primary_key=True)
    Bolt=Column(String(50))
    t1=Column(String(50))
    t2=Column(String(50))
    t3=Column(String(50))
    A=Column(String(50))
    B=Column(String(50))
    C=Column(String(50))
    E=Column(String(50))
    F=Column(String(50))
    H=Column(String(50))
    K=Column(String(50))
    L=Column(String(50))
    W=Column(String(50))
    Type=Column(String(50))

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
    id=Column(Integer,autoincrement=True)
    project_id = Column(String(50), primary_key=True)
    project_name = Column(String(50))    
    project_note = Column(String(500)) 
    user_staffNo = Column(String(50), ForeignKey("user.staffNo"))
    status = Column(String(50))
    user = relationship("User", back_populates="projects", foreign_keys=[user_staffNo])
    
class Material(Base):
   __tablename__="material"
   #id=Column(Integer)╠
   material = Column(String(100),primary_key=True)  
   
class WN_FLG(Base):
    __tablename__="ASME_B16_5_WN_FLG"  
    ref = Column(String(50), primary_key=True)
    classs = Column(String(50))
    nps=Column(String(50))
    flg_od=Column(String(50))
    flg_thk_incld_rf=Column(String(50))
    flg_ht_wn_incld_rf=Column(String(50))
    flg_wt_wn=Column(String(50))
    flg_wt_bld=Column(String(50))
    studs_qty=Column(String(50))
    size_stud=Column(String(100))
    stud_wt=Column(String(50))
    nut_wt=Column(String(50))
    pipe_od=Column(String(50))
    
class Long_WN_FLG(Base):
    __tablename__="ASME_B16_5_Long_WN_FLG"  
    ref = Column(String(50), primary_key=True)
    nps=Column(String(50))
    classs = Column(String(50))    
    bore=Column(String(50))
    neck_od=Column(String(50))
    len_std=Column(String(50))
    std_lg_for_flg_wt=Column(String(50))
    flg_od=Column(String(50))
    flg_thk_incld_rf=Column(String(50))
    std_No_with_ser=Column(String(50))
    std_No_wo_ser=Column(String(50))
    studs_qty=Column(String(50))
    size_stud=Column(String(100))
    stud_wt=Column(String(50))
    nut_wt=Column(String(50))
    stud_plus_2_Nuts=Column(String(50))
    fastners_per_flg=Column(String(50))
    surf_area=Column(String(50))
     
class Saddle(Base):
    __tablename__="Saddle"  
    D = Column(String(50), primary_key=True)
    LB=Column(String(50)) 
    H=Column(String(50)) 
    L1=Column(String(50)) 
    L2=Column(String(50)) 
    Type=Column(String(50)) 
    Max_load=Column(String(50)) 
    approx_wt=Column(String(50)) 
    rib_wt=Column(String(50))    
    
class Saddle_Dim(Base):
    __tablename__="Saddle_Dim"  
    Type = Column(String(50), primary_key=True)
    t1=Column(String(50)) 
    t2=Column(String(50)) 
    L3=Column(String(50)) 
    t3=Column(String(50)) 
    
class Leg_support2(Base):
    __tablename__="Leg_support2"  
    Pipe_size = Column(String(100), primary_key=True)
    A=Column(String(50)) 
    B=Column(String(50)) 
    C=Column(String(50)) 
    E=Column(String(50))
    t=Column(String(50))
    L2000_max_load=Column(String(50))
    L2500_max_load=Column(String(50))
    L3000_max_load=Column(String(50))
    
    
class Vessel(Base):
    __tablename__="Vessel"  
    OD = Column(String(100), primary_key=True)
    A=Column(String(50)) 
    B=Column(String(50)) 
    C=Column(String(50)) 
    E=Column(String(50))
    F=Column(String(50))
    G=Column(String(50)) 
    H=Column(String(50)) 
    J=Column(String(50)) 
    Min_M=Column(String(50)) 
    Min_Anc_Dia=Column(String(50)) 
    X=Column(String(50)) 
    Max_allow_Wt=Column(String(50)) 
    #Pad_Wt=Column(String(50)) 
    #Base_Plt_Wt=Column(String(50)) 
    #Gusset_Wt=Column(String(50))               
   
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



