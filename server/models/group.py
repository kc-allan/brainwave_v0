from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

user_group_association = Table(
    'user_group_association',
    Base.metadata,
    Column('user_id', String(60), ForeignKey('users.id'), primary_key=True, nullable=False),
    Column('group_id', String(60), ForeignKey('groups.id'), primary_key=True, nullable=False)
)

class Group(BaseModel, Base):
    __tablename__ = 'groups'
    name = Column(String(25), nullable=False)
    description = Column(String(128), nullable=False)
    
    group_files = relationship('SharedFile', back_populates='recipient_group', foreign_keys='SharedFile.group_id', cascade='all, delete-orphan')
    
    members = relationship('User', secondary='user_group_association', backref='groups')