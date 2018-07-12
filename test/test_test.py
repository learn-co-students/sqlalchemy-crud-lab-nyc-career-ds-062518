import unittest, sqlite3, sys
sys.path.insert(0, '..')
from states_controller import *

exec(open("./schema.py").read())
connection = sqlite3.connect('states.db')
cursor = connection.cursor()

class TestCreateRead(unittest.TestCase):

    def test_create_ny(self):
        if bool(cursor.execute("SELECT * FROM states WHERE name = 'New York';").fetchall()) == False:
            create_new_york()
        result = [(1, 'New York', 'Albany', 20000000, 0)]
        self.assertEqual(cursor.execute("SELECT * FROM states WHERE name = 'New York';").fetchall(), result)

    def test_create_wyoming(self):
        if bool(cursor.execute("SELECT * FROM states WHERE name = 'Wyoming';").fetchall()) == False:
            create_wyoming()
        result = [(2, 'Wyoming', 'Cheyenne', 579315, 1)]
        self.assertEqual(cursor.execute("SELECT * FROM states WHERE name = 'Wyoming';").fetchall(), result)

    def test_query_all_states(self):
        states = query_all_states()
        self.assertEqual(states[0].name, 'New York')
        self.assertEqual(states[0].capital_city, 'Albany')
        self.assertEqual(states[0].population, 20000000)
        self.assertEqual(states[0].landlocked, False)
        self.assertEqual(states[1].name, 'Wyoming')
        self.assertEqual(states[1].capital_city, 'Cheyenne')
        self.assertEqual(states[1].population, 579315)
        self.assertEqual(states[1].landlocked, True)

    def test_update_cali(self):
        if bool(cursor.execute("SELECT * FROM states WHERE name = 'California';").fetchall()) == False:
            create_cali()
        update_cali()
        cali_pop = cursor.execute("SELECT * FROM states WHERE name = 'California';").fetchall()[0][3]
        self.assertEqual(cali_pop, 50000000)

    def test_delete_connecticut(self):
        if bool(cursor.execute("SELECT * FROM states WHERE name = 'California';").fetchall()) == False:
            create_cali()
        if bool(cursor.execute("SELECT * FROM states WHERE name = 'Connecticut';").fetchall()) == False:
            create_connecticut()
        self.assertEqual(len(cursor.execute("SELECT * FROM states;").fetchall()), 4)

        delete_connecticut()
        self.assertEqual(len(cursor.execute("SELECT * FROM states;").fetchall()), 3)

    def test_rollback_session_changes(self):
        rollback_session_changes()
        self.assertEqual(len(cursor.execute("SELECT * FROM states;").fetchall()), 3)
