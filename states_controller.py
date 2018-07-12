from sqlalchemy import create_engine
from schema import State
from sqlalchemy.orm import sessionmaker
from schema import Base, engine


def create_new_york():
    Session = sessionmaker(bind=engine)
    session = Session()
    new_york = State(name = 'New York', capital_city = 'Albany', population = 20000000, landlocked = False)
    session.add(new_york)
    session.commit()
    # complete the query here

def create_wyoming():
    Session = sessionmaker(bind=engine)
    session = Session()
    wyoming = State(name = 'Wyoming', capital_city = 'Cheyenne', population = 579315, landlocked = True)
    session.add(wyoming)
    session.commit()

def query_all_states():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(State).all()

def create_cali():
    Session = sessionmaker(bind=engine)
    session = Session()
    cali = State(name="California", capital_city="Sacramento", population=40000000, landlocked=False)
    session.add(cali)
    session.commit()

def update_cali():
    Session = sessionmaker(bind=engine)
    session = Session()
    california = session.query(State).filter_by(name = "California").update({"population":50000000})
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
    conn = session.query(State.name).filter_by(name = "Connecticut").delete()
    session.commit()

def rollback_session_changes():
    Session = sessionmaker(bind=engine)
    session = Session()
    west_dakota = State(name="West Dakota", capital_city="Fake City", population=123456, landlocked=True)
    session.add(west_dakota)
    session.rollback()
