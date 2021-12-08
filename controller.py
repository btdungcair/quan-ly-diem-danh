import time
from helper import sort_by_name, image_to_octet_string
import sqlite3
from sqlite3 import Error
import os

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

def get_sorted_students_list():
    return sort_by_name(get_students_list())

def get_student(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_student(id, fullname, gender, dob, absent_count, image_path):
    conn = create_connection()
    cur = conn.cursor()
    image = image_to_octet_string(image_path)
    cur.execute("INSERT INTO students (id, fullname, gender, dob, absent_count, image) VALUES (?, ?, ?, ?, ?, ?)", (id, fullname, gender, dob, absent_count, image))
    conn.commit()
    cur.close()
    conn.close()

def update_student(old_id, id, fullname, gender, dob, absent_count, image_data):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET id=?, fullname=?, gender=?, dob=?, absent_count=?, image=? WHERE id=?", (id, fullname, gender, dob, absent_count, image_data, old_id))
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

def valid_id(id):
    student_list = get_students_list()
    if len(student_list) == 0:
        return True
    id_list = [student[0] for student in student_list]
    return not id in id_list and id.isdigit() and len(str(id)) == 8

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

def update_attendance(student_id, new_student_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE attendance SET student_id=? WHERE student_id=?", (new_student_id, student_id))
    conn.commit()
    cur.close()
    conn.close()

# if __name__ == '__main__':
#     print(get_students_list())