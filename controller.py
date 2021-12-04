import time
import sqlite3
from sqlite3 import Error

def create_connection(db_file="test.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def check_login(username, password):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if len(rows) == 1:
        return True
    else:
        return False

def get_students_list():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_date():
    date = time.strftime("%d/%m/%Y")
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO dates (date) VALUES (?)", (date,))
    conn.commit()
    cur.close()
    conn.close()

def attendance(student_id_set, date=time.strftime("%d/%m/%Y")):
    conn = create_connection()
    cur = conn.cursor()
    for student_id in student_id_set:
        cur.execute("INSERT INTO attendance (student_id, date) VALUES (?, ?)", (student_id, date))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    print('done')