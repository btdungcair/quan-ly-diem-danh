import time
import helper
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

def get_sorted_students_list():
    return helper.sort_by_name(get_students_list())

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
    image = helper.image_to_octet_string(image_path)
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

def update_absent_count(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET absent_count=absent_count+1 WHERE id=?", (id,))
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
def add_date(date=time.strftime("%d/%m/%Y")):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO dates (date) VALUES (?)", (date,))
    conn.commit()
    cur.close()
    conn.close()

def get_dates_list():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM dates")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    dates = [date[0] for date in rows]
    return sorted(dates, key=lambda date: time.strptime(date, "%d/%m/%Y"))

# Table attendance
def attendance(student_id_set, date=time.strftime("%d/%m/%Y")):
    conn = create_connection()
    cur = conn.cursor()
    for student_id in student_id_set:
        cur.execute("INSERT INTO attendance (student_id, date) VALUES (?, ?)", (student_id, date))
    conn.commit()
    cur.close()
    conn.close()
    absentee_list = [student for student in get_students_list() if student[0] not in student_id_set]
    for student in absentee_list:
        update_absent_count(student[0])

def update_attendance(student_id, new_student_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE attendance SET student_id=? WHERE student_id=?", (new_student_id, student_id))
    conn.commit()
    cur.close()
    conn.close()

def get_attendance(student_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT date FROM attendance WHERE student_id=?", (student_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    dates = [date[0] for date in rows]
    dates = sorted(dates, key=lambda date: time.strptime(date, "%d/%m/%Y"))
    res = []
    for date in get_dates_list():
        if date in dates:
            res.append("x")
        else:
            res.append("vắng")
    return res

if __name__ == "__main__":
    date = "23/12/2021"
    add_date(date)
    attendance({18000267, 18000321, 19000345, 20000145}, date)
    print(get_attendance(19000470))