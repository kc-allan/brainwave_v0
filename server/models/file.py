from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class File(BaseModel, Base):
    __tablename__ = 'files'
    filename = Column(String(60), nullable=False)
    filepath = Column(String(60), nullable=False)
    owner_id = Column(String(60), ForeignKey('users.id'))
    
    owner = relationship('User', back_populates='owned_files', foreign_keys='File.owner_id')
    
class SharedFile(File):
    recipient_user = relationship('User', back_populates='saved_files', viewonly=False, foreign_keys='SharedFile.user_id')
    user_id = Column(String(60), ForeignKey('users.id'))
    recipient_group = relationship('Group', back_populates='group_files', foreign_keys='SharedFile.group_id')
    group_id = Column(String(60), ForeignKey('groups.id'))