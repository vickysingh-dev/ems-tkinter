import psycopg2
import configparser

config = configparser.ConfigParser()
config.read(".\config.ini")
dbparam = config["postgresql"]


def fetch(insert_script, insert_value=False):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=dbparam["host"],
            dbname=dbparam["dbname"],
            user=dbparam["user"],
            password=dbparam["password"],
            port=dbparam["port"]
        )
        cur = conn.cursor()

        # create_script = '''CREATE TABLE IF NOT EXISTS employee(
        #     id SERIAL,
        #     first_name varchar(50) NOT NULL,
        #     last_name varchar(50) NOT NULL,
        #     gender varchar(50) NOT NULL,
        #     designation varchar(50) NOT NULL,
        #     phone int PRIMARY KEY,
        #     email varchar(50) NOT NULL,
        #     doj DATE NOT NULL,
        #     salary int NOT NULL
        # )'''
        # cur.execute(create_script)

        # insert_script = 'INSERT INTO employee (first_name, last_name, gender, designation, phone, email, doj, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        # insert_value = ('vicky', 'singh', 'male', 'developer', 999,
        #                 'vickysingh@gmail.com', '2023-02-01', 90000)
        # cur.execute(insert_script, insert_value)

        if insert_value:
            cur.execute(insert_script, insert_value)
        else:
            cur.execute(insert_script)
            result = cur.fetchone()

        conn.commit()

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
        return result


def login(id, password):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=dbparam["host"],
            dbname=dbparam["dbname"],
            user=dbparam["user"],
            password=dbparam["password"],
            port=dbparam["port"]
        )
        cur = conn.cursor()

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
