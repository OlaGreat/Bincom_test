import psycopg2
from datetime import date
import time

timecreated = time.strftime("%H:%M:%S", time.localtime())


def connect_db():
    conn = psycopg2.connect(database="railway", user="postgres", password = "4C-3eB2-beaEe545D62bgbFbdaccAD3c",
                 host ="monorail.proxy.rlwy.net", port="39598")
                     
    return conn



def create_Table():
    conn = connect_db()
    cursor = conn.cursor()

    sql='''CREATE TABLE todoList(
                             ID SERIAL PRIMARY KEY,
                             TODO CHAR(50),
                             DATECREATED CHAR(10),
                             TIMECREATED CHAR(10)
                            )'''
    cursor.execute(sql)
    conn.commit()
    cursor.close()



def create_to_do_List(todo):
    conn = connect_db()
    cursor = conn.cursor()
    script ='''INSERT INTO todoLIST(TODO,DATECREATED,TIMECREATED)
                VALUES(%s, %s, %s)'''
    
    palceholder_value =(todo, date.today(), timecreated)
    cursor.execute(script, palceholder_value)
    conn.commit()
    conn.close()

def find_to_do(todo_id):
    conn = connect_db()
    cursor = conn.cursor()
    script = ''' SELECT * FROM todoList WHERE ID = %s
                '''
    cursor.execute(script, (todo_id,))
    found_todo = cursor.fetchone()
    conn.close()
    return found_todo

def update_todo(todo_id, todo):
    conn = connect_db()
    cursor = conn.cursor()
    script = '''UPDATE todoList set todo = %s WHERE ID = %s RETURNING *'''
    cursor.execute(script, (todo, todo_id))
    updated_todo = cursor.fetchone()
    conn.commit()
    conn.close()
    return updated_todo

def delete_todo(todo_id):
    conn = connect_db()
    cursor = conn.cursor()
    script = '''DELETE FROM todoList WHERE ID = %s'''

    cursor.execute(script, (todo_id,))
    conn.commit()
    cursor.close()





create_to_do_List("i have to submmit this before 12am")
found_todo = find_to_do(1)
print(found_todo)
updated_todo = update_todo(1, "i must be happy today")
print(updated_todo)
delete_todo(1)
