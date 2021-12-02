import sqlite3
from sqlite3 import Error

def check_login(username, password):
    conn = None
    try:
        conn = sqlite3.connect("test.db")
    except Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
    rows = cur.fetchall()
    if len(rows) == 1:
        return True
    else:
        return False

# if __name__ == '__main__':
#     show_all_data()