from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.group import user_group_association

class User(BaseModel, Base):
    __tablename__ = 'users'
    username = Column(String(60), nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    _password = Column("password", String(128), nullable=False)
    
    owned_files = relationship('File', back_populates='owner', cascade='all, delete-orphan', viewonly=False, foreign_keys='File.owner_id')
    saved_files = relationship('SharedFile', back_populates='recipient_user', cascade='all, delete', foreign_keys='SharedFile.user_id')