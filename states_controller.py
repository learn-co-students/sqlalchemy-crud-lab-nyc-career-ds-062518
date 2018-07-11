from sqlalchemy import create_engine
from schema import State
from sqlalchemy.orm import sessionmaker
from schema import Base, engine

engine = create_engine('sqlite:///states.db', echo=True)

def create_new_york():
    Session = sessionmaker(bind=engine)
    session = Session()
    ny= State(name='New York', capital_city='Albany', population=20000000, landlocked=False)
    session.add(ny)
    session.commit()

    # complete the query here

def create_wyoming():
    Session = sessionmaker(bind=engine)
    session = Session()
    wy = State(name='Wyoming', capital_city='Cheyenne', population=579315, landlocked= True)
    session.add(wy)
    session.commit()

def query_all_states():
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    return states

def create_cali():
    Session = sessionmaker(bind=engine)
    session = Session()
    cali = State(name="California", capital_city="Sacramento", population=40000000, landlocked=False)
    session.add(cali)
    session.commit()

def update_cali():
    Session = sessionmaker(bind=engine)
    session = Session()
    cali = session.query(State).filter_by(name='California').first()
    cali.population = 50000000
    session.commit()

def create_connecticut():
    Session = sessionmaker(bind=engine)
    session = Session()
    ct = State(name="Connecticut", capital_city="Hartford", population=3600000, landlocked=False)
    session.add(ct)
    session.commit()

def delete_connecticut():
    Session = sessionmaker(bind=engine)
    session = Session()
    ct = session.query(State).filter_by(name= 'Connecticut').first()
    session.delete(ct)
    session.commit()

def rollback_session_changes():
    Session = sessionmaker(bind=engine)
    session = Session()
    west_dakota = State(name="West Dakota", capital_city="Fake City", population=123456, landlocked=True)
    session.add(west_dakota)
    session.rollback()
    session.commit()
