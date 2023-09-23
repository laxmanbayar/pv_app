# from ..DataBase.models import Project,User
# from ..DataBase.DB_config import DB_config_class

from DataBase.common_models import User
from DataBase.DB_config import DB_config_class




session=DB_config_class.session

def auth_user(uname):
    
    user=session.query(User).filter_by(staffNo=uname).first()
    return user