from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(INTEGER, primary_key = True)
    name = Column(TEXT)
    capital_city = Column(TEXT)
    population = Column(INTEGER)
    landlocked = Column(BOOLEAN)

    

engine = create_engine('sqlite:///states.db', echo=True)
Base.metadata.create_all(engine)
