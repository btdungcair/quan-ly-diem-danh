import time
import locale
import sqlite3
from sqlite3 import Error

def create_connection(db_file="test.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

# Table user
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

# Table students
def get_students_list():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_student(id, fullname, dob, absent_count):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (id, fullname, dob, absent_count) VALUES (?, ?, ?, ?)", (id, fullname, dob, absent_count))
    conn.commit()
    cur.close()
    conn.close()

def update_student(id, fullname, dob, absent_count):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET id=?, fullname=?, dob=?, absent_count=? WHERE id=?", (id, fullname, dob, absent_count, id))
    conn.commit()
    cur.close()
    conn.close()

def delete_student(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    cur.close()
    conn.close()

# Table dates
def add_date():
    date = time.strftime("%d/%m/%Y")
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO dates (date) VALUES (?)", (date,))
    conn.commit()
    cur.close()
    conn.close()

# Table attendance
def attendance(student_id_set, date=time.strftime("%d/%m/%Y")):
    conn = create_connection()
    cur = conn.cursor()
    for student_id in student_id_set:
        cur.execute("INSERT INTO attendance (student_id, date) VALUES (?, ?)", (student_id, date))
    conn.commit()
    cur.close()
    conn.close()

################################################################################
def getName(s):
    s = s.split()
    lname = s[0]
    fname = s[-1]
    return (lname, fname)
    
def compare(name):
    locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
    lname = getName(name)[0]
    fname = getName(name)[1]
    return locale.strxfrm(fname), locale.strxfrm(lname)

def sort_by_name(student_list):
    """
    Sort students list by name in Vietnamese alphabet
    """
    student_list.sort(key=lambda x: compare(x[1]))
    return student_list

# if __name__ == '__main__':
#     lst = get_students_list()
#     print(sort_by_name(lst))