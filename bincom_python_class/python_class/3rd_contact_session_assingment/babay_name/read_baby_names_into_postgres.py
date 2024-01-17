import psycopg2


def connect_db():
    conn = psycopg2.connect(database ="railway",user ="postgres",  password ="4C-3eB2-beaEe545D62bgbFbdaccAD3c",  
                            host ="monorail.proxy.rlwy.net",port ="39598")
    return conn   

def create_Table():
    conn = connect_db()
    cursor = conn.cursor()
    script = ''' CREATE TABLE baby_name 
                ( ID SERIAL PRIMARY KEY,
                    FIRST_NAME CHAR(20),
                    LAST_NAME CHAR(20)
                )'''
    cursor.execute(script)
    conn.commit()
    cursor.close()

def insert_into_table():
    conn = connect_db()
    cursor = conn.cursor()
    script = '''INSERT INTO baby_name(first_name, last_name)
                VALUES(%s, %s)
            '''
    with open("baby_names.txt") as file:
        for names in file:
            first_name, last_name = names.strip().split(' ')
            cursor.execute(script, (first_name, last_name))
    conn.commit()
    cursor.close()


insert_into_table()
            