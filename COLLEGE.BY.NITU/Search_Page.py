from tkinter import *  
import random
import Marksheet_Backend
import Marksheet_Frontend
import tkinter.messagebox
import os

class Window_1():
       def __init__(self, master):
              self.master = master
              self.master.title('Search Page')
              self.master.geometry('1360x750')
              self.master.config(bg = 'navajowhite')

              self.roll = StringVar()
              frame = LabelFrame(self.master, width = 1000, height = 100, font = ('arial',30,'bold'), relief = 'ridge', bd = 15, bg = 'wheat')
              frame.grid(row = 1, column = 0, padx = 200, pady = 200)

              label = Label(frame, text = 'Enter Roll Number', font = ('arial',25,'bold'), bg = 'wheat' )
              label.grid(row = 0, column = 0, padx = 100, pady = 10)

              entry = Entry(frame, font = ('arial',25,'bold'), textvariable = self.roll)
              entry.grid(row = 0, column = 1, padx = 30, pady = 20)

              def Search():
                     if(len(self.roll.get()) != 0):
                           row = Marksheet_Backend.search(int(self.roll.get()))
                           print(row)
                           Marksheet_Frontend.search_result_marksheet(row)
                     else:
                            tkinter.messagebox.askokcancel('Attention','Please enter valid Roll No.')
                            return

              def new():
                     filename = 'Marksheet_Frontend.py'
                     os.system(filename)
                     os.system('notepad'+filename)
                           

              btnSearch = Button(frame, text = 'SEARCH', width = 15, font = ('arial',15,'bold'), command=Search)
              btnSearch.grid(row = 1, column = 0, padx = 50)
              btnNew = Button(frame, text = 'CREATE NEW', width = 15, font = ('arial',15,'bold'), command=new)
              btnNew.grid(row = 1, column = 1, padx = 50, pady = 20 )




root = Tk()
root.title("Login Form")
Window_1(root)
root.mainloop()
