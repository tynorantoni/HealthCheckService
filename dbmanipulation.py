import psycopg2
from dbconnector import connect_to_db

# basic DB manipulation functions

def create_table():
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute('''CREATE TABLE ping_data
        (id SERIAL PRIMARY KEY NOT NULL,
        date_of_ping TIMESTAMP,
        BSS TEXT,
        KSS TEXT,
        WCS TEXT,
        DAS TEXT,
        UIS TEXT
        );'''
                    )

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        cur.close()
        conn.close()


def drop_table():
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute('''DROP TABLE ping_data;''')
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        cur.close()
        conn.close()


def insert_status_to_db(connection, **kwargs):
    try:
        cur = connection.cursor()

        cur.execute('''INSERT INTO ping_data (
        date_of_ping,BSS,KSS,WCS,DAS,UIS
                ) VALUES ('{}','{}','{}','{}','{}','{}');'''.format(
            kwargs['date_of_ping'],
            kwargs['BSS'],
            kwargs['KSS'],
            kwargs['WCS'],
            kwargs['DAS'],
            kwargs['UIS']
        ))

        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)