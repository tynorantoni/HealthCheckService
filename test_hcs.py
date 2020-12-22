import psycopg2
import pytest
import requests

from requests import RequestException

from dbconnector import connect_to_db



class TestClass:

    # setup db connection
    @pytest.fixture()
    def setUp(self):
        connection = connect_to_db()
        yield connection
        connection.close()

    # connect to DB
    def test_connect_to_db(self, setUp):

        cur = setUp.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        assert db_version is not None

    # create table for testing
    def test_create_table(self, setUp):

        cur = setUp.cursor()

        cur.execute('''CREATE TABLE ping_data_test_table
                (id SERIAL PRIMARY KEY NOT NULL,
        date_of_ping TIMESTAMP,
        BSS TEXT,
        KSS TEXT,
        WCS TEXT,
        DAS TEXT,
        UIS TEXT
        );'''
                    )

        setUp.commit()
        cur.execute('SELECT * FROM ping_data_test_table;')
        assert cur.fetchone() is None

    # insert mocked data to DB
    def test_insert_to_db(self, setUp):

        cur = setUp.cursor()

        cur.execute('''INSERT INTO ping_data_test_table (
                date_of_ping,BSS,KSS,WCS,DAS,UIS				
                ) VALUES (
					'2020-05-28 19:00:00', 
					'pong',
					'pong',
					'pong',
					'pong',
					'dead'
        );''')

        rows = cur.rowcount
        setUp.commit()
        assert 1 == rows

    # drop test table after tests
    def test_drop_table(self, setUp):
        try:
            cur = setUp.cursor()

            cur.execute('''DROP TABLE ping_data_test_table;''')
            setUp.commit()
            assert cur.statusmessage == 'DROP TABLE'
        except psycopg2.DatabaseError as error:
            print(error)

    # testing Accuweather API
    def test_get_health_status(self):
        list_of_services = {
            'BSS': 'http://127.0.0.1:5000/ping',
            'KSS': 'http://127.0.0.1:5000/ping',
            'WCS': 'http://127.0.0.1:5000/ping',
            'DAS': 'http://127.0.0.1:5000/ping',
            'UIS': 'http://127.0.0.1:5050/ping'
        }
        try:
            dict_of_requests = {}
            for service in list_of_services:
                try:
                    request = requests.get(list_of_services[service])
                    dict_of_requests[service] = request.text

                except Exception as exc:
                    print("failure ", exc)
                    dict_of_requests[service] = 'dead'


            assert len(dict_of_requests)==5
            assert dict_of_requests['BSS']=='pong' or dict_of_requests['BSS']=='dead'

        except RequestException as error:
            print(error)



if __name__ == '__main__':
    pytest.main()
