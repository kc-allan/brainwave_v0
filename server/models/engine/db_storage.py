from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.user import User
from models.group import Group
from models.file import File
from models.base_model import Base


name2classs = {
    'User': User,
    'Group': Group,
    'File': File
}

class DBStorage:
    __session = None
    __engine = None
    
    def __init__(self) -> None:
        dbuser = 'brainwave_dev'
        dbname = 'brainwave_db'
        dbhost = 'localhost'
        dbpasswd = 'brainwave_dev_pwd'
        self.__engine = create_engine(
            f'mysql+mysqldb://{dbuser}:{dbpasswd}@{dbhost}/{dbname}',
            pool_pre_ping=False
		)
    
    def reload(self):
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)
    
    def save(self):
        self.__session.commit()
    
    def new(self, obj):
        self.__session.add(obj)
        
    def delete(self, obj):
        self.__session.delete(obj)
        
    def get(self, obj, id):
        if obj is not None and id is not None:
            if type(obj) == str:
                obj = name2classs[obj]
        print(obj,id)
        return self.__session.query(obj).filter_by(id=id).first()

    def all(self, obj=None):
        if not obj == None:
            return self.__session.query(obj).all()
        return self.__session.query().all()