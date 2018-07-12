from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    capital_city = Column(Text)
    population = Column(Integer)
    landlocked = Column(Boolean)

engine = create_engine('sqlite:///states.db', echo=True)
Base.metadata.create_all(engine)
