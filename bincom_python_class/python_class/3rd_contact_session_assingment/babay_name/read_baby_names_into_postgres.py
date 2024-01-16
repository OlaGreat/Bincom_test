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


# create_Table()
    
with open("baby_names.txt") as file:
    for names in file:
       for n in names.split():
        print(n)

