#from peewee import *
#from Initial_Schema import User
#from dotenv import dotenv_values
import os
import pymysql
from DB_config import DB_config_class
import sqlite3


#db_name='PV_BOM'

class PV_DB_creation:
    def __init__(self):
        self.config=DB_config_class.config
        self.db_name=self.config['DB_NAME']
             
    def create_db(self):
        host=self.config['DB_HOST']
        port=int(self.config['DB_PORT'])
        user=self.config['DB_USER']
        pwd=self.config['DB_PASSWORD']
        mode=self.config['MODE']
        
        if(mode=='prod'):
            try:
                conn = pymysql.connect(host=host, port=port,user=user, password=pwd)
                conn.cursor().execute(f'CREATE DATABASE IF NOT EXISTS {self.db_name}')
                conn.close()
            except Exception as e:
                #raise e
                conn.rollback()
            # end try
            
            
        elif(mode=='dev'):
            try:
                print(self.db_name)
                _db_name=self.db_name+'.db'
                conn=sqlite3.connect(_db_name)
               
            except Exception as e:
                raise e
            # end try
            
            
            
if __name__=='__main__':
    
    #db_name='PV_BOM'
    new_db_creation=PV_DB_creation()
    db=new_db_creation.create_db()
    
                
            
#User.create(staff_no='6209254',pwd='6209254',name='laxman')

