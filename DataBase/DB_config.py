from dotenv import dotenv_values
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DB_config_class:
    config=dotenv_values('.env')
    user=config['DB_USER']
    pwd=config['DB_PASSWORD']
    host=config['DB_HOST']
    port=config['DB_PORT']
    db_name=config['DB_NAME']
    mode=config['MODE']
    db_url=None
    if(mode=='prod'):
        db_url=f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db_name}"
    elif(mode=='dev'):
        db_url=f"sqlite:///{db_name+'.db'}" 
    
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()  
    Base=declarative_base()    
        