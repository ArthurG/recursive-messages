from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Template(Base):
	__tablename__ = 'Template'
	id = Column(Integer, primary_key =True)
	placeholder = Column(String(250))
	permanent = Column(Boolean)
	replacementName = Column(String(250))
	replacementText = Column(String(99999))
engine = create_engine('sqlite:///sqlalchemy.db')

Base.metadata.create_all(engine)

