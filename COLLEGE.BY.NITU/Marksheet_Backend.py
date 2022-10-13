from tkinter import*
import sqlite3

def connect():
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS Marks (id INTEGER PRIMARY KEY, name text, roll integer, fname text, mname \
                     text, DOB integer, gender text, scl text, email text, m1 integer, m2 integer, m3 integer, m4 integer, \
                     m5 integer, gt integer, per integer, cgpa integer, grade text, div text, result text)')

       con.commit()
       con.close()

def insert(name = ' ',roll = ' ',fname = ' ',mname = ' ',DOB = ' ',gender = ' ',scl = ' ',email = ' ',m1 = ' ',m2 = ' ', \
           m3 = ' ',m4 = ' ',m5 = ' ',gt = ' ',per = ' ',cgpa = ' ',grade = ' ', div = ' ', result = ' '):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('INSERT INTO Marks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name,roll,fname,mname,DOB,gender, \
                                                                                        scl,email,m1,m2,m3,m4,m5,gt,per,\
                                                                                        cgpa,grade,div,result))

       con.commit()
       con.close()

'''def view():
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM Marks')

       con.commit()
       con.close()

def delete(id):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('DELETE FROM Marks WHERE id = ?)',(id,))

       con.commit()
       con.close()'''

def update(id,name = ' ',roll = ' ',fname = ' ',mname = ' ',DOB = ' ',gender = ' ',scl = ' ',email = ' ',m1 = ' ',m2 = ' ', \
           m3 = ' ',m4 = ' ',m5 = ' ',gt = ' ',per = ' ',cgpa = ' ',grade = ' ', div = ' ', result = ' '):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('UPDATE Marks SET name = ? OR roll = ? OR fname =  ? OR mname = ? OR DOB = ? OR gender = ? OR \
                     scl = ? OR email = ? OR m1 = ? OR m2 = ? OR  m3 = ? OR m4 = ? OR m5 = ? OR gt = ? OR per = ? OR \
                     cgpa = ? OR grade = ? OR div = ? OR result = ?',(name,roll,fname,mname,DOB,gender,scl,email,m1,m2,m3, \
                                                                      m4,m5,gt,per,cgpa,grade))

       con.commit()
       con.close()

def search(roll):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM Marks WHERE roll = ?',(roll,))
       row = cur.fetchall()
       return row     

connect()

