import sqlite3

def connect():
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, recpt integer, name text, admsn text, date integer, \
                    branch text, sem text, total integer, paid integer, due integer)')

       con.commit()
       con.close()

def insert(recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('INSERT INTO fee VALUES (NULL,?,?,?,?,?,?,?,?,?)',(recpt,name,admsn,date,branch,sem,total,paid,due))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee')
       row = cur.fetchall()
       return row

       con.commit()
       

def delete(id):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('DELETE FROM fee WHERE id = ?',(id,))

       con.commit()
       con.close()

def update(id,recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('UPDATE fee SET recpt = ? OR name = ? OR admsn = ? OR date = ? OR branch = ? OR sem = ? OR total = ? OR \
                    paid = ? OR due = ?',(recpt,name,admsn,date,branch,sem,total,paid,due))


       con.commit()
       con.close()

def search(recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee WHERE  recpt = ? OR name = ? OR admsn = ? OR date = ? OR branch = ? OR sem = ? OR \
                    total = ? OR paid = ? OR due = ?',(recpt,name,admsn,date,branch,sem,total,paid,due))
       row = cur.fetchall()
       return row

       con.commit()
       
connect()


