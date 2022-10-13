from tkinter import*
import tkinter.messagebox  
import random
import Std_info_BackEnd
from tkinter import ttk

class Std_info():
       def __init__(self, master):
              self.master = master
              self.master.title('Student Information')
              self.master.geometry('1350x750')
              self.master.config(bg = 'navajowhite')
              
              def information():
              #========================================================Variables=====================================================================
                     self.name = StringVar()
                     self.fname = StringVar()
                     self.mname = StringVar()
                     self.address = StringVar()
                     self.mobno = StringVar()
                     self.email = StringVar()
                     self.dob = StringVar()
                     self.gender = StringVar()
                     


               #==========================================================Functions====================================================================
                     def StudentRec(event):
                            try: 
                                   global selected_tuple
                                   
                                   index = self.listbox.curselection()[0]
                                   selected_tuple = self.listbox.get(index)

                                   self.Entry_name.delete(0, END)
                                   self.Entry_name.insert(END, selected_tuple[1])
                                   self.Entry_fname.delete(0, END)
                                   self.Entry_fname.insert(END, selected_tuple[2])
                                   self.Entry_mname.delete(0, END)
                                   self.Entry_mname.insert(END, selected_tuple[3])
                                   self.Entry_address.delete(0, END)
                                   self.Entry_address.insert(END, selected_tuple[4])
                                   self.Entry_mobno.delete(0, END)
                                   self.Entry_mobno.insert(END, selected_tuple[5])
                                   self.Entry_emailID.delete(0, END)
                                   self.Entry_emailID.insert(END, selected_tuple[6])
                                   self.Entry_dob.delete(0, END)
                                   self.Entry_dob.insert(END, selected_tuple[7])
                                   self.Entry_gender.delete(0, END)
                                   self.Entry_gender.insert(END, selected_tuple[8])
                            except IndexError:
                                   pass


                     def Add():
                            if(len(self.name.get()) != 0):
                               Std_info_BackEnd.insert(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                       self.gender.get())
                               self.listbox.delete(0, END)
                               self.listbox.insert(END, (self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                       self.gender.get()))

                     def Display():
                               self.listbox.delete(0, END)
                               for row in Std_info_BackEnd.view():
                                      self.listbox.insert(END, row, str(' '))


                     def Exit():
                            Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                            if Exit > 0:
                                   self.master.destroy()
                                   return 
                            

                     def Reset():
                            self.name.set('')
                            self.fname.set('')
                            self.mname.set('')
                            self.address.set('')
                            self.mobno.set('')
                            self.email.set('')
                            self.dob.set('')
                            self.gender.set('')
                            self.listbox.delete(0, END)

                     

                     def Delete():
                            if(len(self.name.get()) != 0):
                               Std_info_BackEnd.delete(selected_tuple[0])
                               Reset()
                               Display()


                     def Search():
                            self.listbox.delete(0, END)
                            for row in Std_info_BackEnd.search(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(),self.gender.get()):
                                   self.listbox.insert(END, row, str(' '))
                                   

                     def Update():
                            if(len(self.name.get()) != 0):
                               Std_info_BackEnd.delete(selected_tuple[0])
                            if(len(self.name.get()) != 0):
                               Std_info_BackEnd.insert(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                       self.gender.get())

                               self.listbox.delete(0, END)
                               self.listbox.insert(END, (self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                       self.gender.get()))
                     


                     #============================================================Frames=====================================================================

                     self.Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                  bg = 'navajowhite',bd = 15, relief = 'ridge')
                     self.Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                     self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT INFORMATION ')
                     self.Frame_1.grid(row = 1, column = 0, padx = 10)

                     self.Frame_2 = LabelFrame(self.Main_Frame, width = 750, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT DATABASE')
                     self.Frame_2.grid(row = 1, column = 1, padx = 5)                  
                     
                     self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                                               bg = 'navajowhite', relief = 'ridge', bd = 13)
                     self.Frame_3.grid(row = 2, column = 0, pady = 10)


                     
                     #========================================================Labels of Frame_1========================================================
                     self.Label_name = Label(self.Frame_1, text = 'Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                     self.Label_fname = Label(self.Frame_1, text = 'Father Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_fname.grid(row = 1, column = 0, sticky = W, padx = 20)
                     self.Label_mname = Label(self.Frame_1, text = 'Mother Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_mname.grid(row = 2, column = 0, sticky = W, padx = 20)
                     self.Label_address = Label(self.Frame_1, text = 'Address', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_address.grid(row = 3, column = 0, sticky = W, padx = 20)
                     self.Label_mobno = Label(self.Frame_1, text = 'Mobile Number', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 20)
                     self.Label_emailID = Label(self.Frame_1, text = 'Email ID', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 20)
                     self.Label_dob = Label(self.Frame_1, text = 'Date of Birth', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_dob.grid(row = 6, column = 0, sticky = W, padx = 20)
                     self.Label_gender = Label(self.Frame_1, text = 'Gender', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)


                     #========================================================Entries of Frame_1========================================================
                     self.Entry_name = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.name)
                     self.Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                     self.Entry_fname = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.fname)
                     self.Entry_fname.grid(row = 1, column = 1, padx = 10, pady = 5)
                     self.Entry_mname = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.mname)
                     self.Entry_mname.grid(row = 2, column = 1, padx = 10, pady = 5)
                     self.Entry_address = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.address)
                     self.Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                     self.Entry_mobno = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.mobno)
                     self.Entry_mobno.grid(row = 4, column = 1, padx = 10, pady = 5)
                     self.Entry_emailID = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.email)
                     self.Entry_emailID.grid(row = 5, column = 1, padx = 10, pady = 5)
                     self.Entry_dob = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.dob)
                     self.Entry_dob.grid(row = 6, column = 1, padx = 10, pady = 5)
                     self.Entry_gender = ttk.Combobox(self.Frame_1, values = (' ','Male','Female','Others'),\
                                                      font = ('arial',17,'bold'), textvariable = self.gender, width = 19)
                     self.Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)




                     #========================================================Buttons of self.Frame_3=========================================================
                     self.btnSave = Button(self.Frame_3, text = 'SAVE', font = ('arial',17,'bold'), width = 8, command = Add)
                     self.btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
                     self.btnDisplay = Button(self.Frame_3, text = 'DISPLAY', font = ('arial',17,'bold'), width = 8, command = Display)
                     self.btnDisplay.grid(row = 0, column = 1, padx = 10, pady = 10)
                     self.btnReset = Button(self.Frame_3, text = 'RESET', font = ('arial',17,'bold'), width = 8, command = Reset)
                     self.btnReset.grid(row = 0, column = 2, padx = 10, pady = 10)
                     self.btnUpdate = Button(self.Frame_3, text = 'UPDATE', font = ('arial',17,'bold'), width = 8, command = Update)
                     self.btnUpdate.grid(row = 0, column = 3, padx = 10, pady = 10)
                     self.btnDelete = Button(self.Frame_3, text = 'DELETE', font = ('arial',17,'bold'), width = 8, command = Delete)
                     self.btnDelete.grid(row = 0, column = 4, padx = 10, pady = 10)
                     self.btnSearch = Button(self.Frame_3, text = 'SEARCH', font = ('arial',17,'bold'), width = 8, command = Search )
                     self.btnSearch.grid(row = 0, column = 5, padx = 10, pady = 10)
                     self.btnExit = Button(self.Frame_3, text = 'EXIT', font = ('arial',17,'bold'), width = 8, command = Exit)
                     self.btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)



                     #===============================================List Box and self.scrollbar========================================================
                     self.scrollbar = Scrollbar(self.Frame_2)
                     self.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                     self.listbox = Listbox(self.Frame_2, width = 75, height = 20 , font = ('arial',12,'bold'))
                     self.listbox.bind('<<ListboxSelect>>', StudentRec)
                     self.listbox.grid(row = 0, column = 0)
                     self.scrollbar.config(command = self.listbox.yview)
                            
              information()
                     

root = Tk()
obj = Std_info(root)
root.mainloop()
