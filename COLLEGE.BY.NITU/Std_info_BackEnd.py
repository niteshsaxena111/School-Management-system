import sqlite3

def connect():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, fname text, mname text, \
                     address text, mobno integer,email text, dob integer, gender text)")

       conn.commit()
       conn.close()

def insert(name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (name, fname, mname, address , mobno, email, dob, gender))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM student WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id,name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("UPDATE student SET name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? OR gender = ?", \
                   (name, fname, mname, address , mobno, email, dob, gender))

       conn.commit()
       conn.close()

def search(name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student WHERE name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? \
                     OR gender = ?", (name, fname, mname, address , mobno, email, dob, gender))
       rows = cur.fetchall()
       return rows
       
       conn.close()

                                                               
connect()
       
