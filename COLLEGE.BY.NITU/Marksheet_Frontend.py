from tkinter import *  
import random
import Marksheet_Backend
import tkinter.messagebox
from tkinter import ttk

def marksheet():
       root = Tk()
       root.title('Marksheet')
       root.geometry('1350x750')
       root.config(bg = 'Navajo white')

       #================================================Variables======================================================
       name = StringVar()
       roll = StringVar()
       fname = StringVar()
       mname = StringVar()
       DOB = StringVar()
       gender = StringVar()
       scl = StringVar()
       email = StringVar()
       m1 = DoubleVar()
       m2 = DoubleVar()
       m3 = DoubleVar()
       m4 = DoubleVar()
       m5 = DoubleVar()
       gt = DoubleVar()
       per = DoubleVar()
       cgpa = DoubleVar()
       grade = StringVar()
       div = StringVar()
       result = StringVar()


       #==============================================Functions==========================================================
       def Add():
              if (len(roll.get()) != 0):
                     Marksheet_Backend.insert(name.get(),roll.get(),fname.get(),mname.get(),DOB.get(),gender.get(), \
                                              scl.get(),email.get(),m1.get(),m2.get(),m3.get(),m4.get(),m5.get(), \
                                              gt.get(),per.get(),cgpa.get(),grade.get(),div.get(),result.get())

       def Update():
              if (len(roll.get()) != 0):
                     Marksheet_Backend.update(name.get(),roll.get(),fname.get(),mname.get(),DOB.get(),gender.get(), \
                                              scl.get(),email.get(),m1.get(),m2.get(),m3.get(),m4.get(),m5.get(), \
                                              gt.get(),per.get(),cgpa.get(),grade.get(),div.get(),result.get())
                    
       def Exit():
              Exit = tkinter.messagebox.askyesno('Marksheet','Confirm if you want to Exit')
              if Exit > 0:
                     root.destroy()
                     return

       
       def Compute():
              x1 = (m1.get());      x2 = (m2.get());    x3 = (m3.get());      x4 = (m4.get());    x5 = (m5.get())

              if x1 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x2 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x3 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x4 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x5 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
                     
       
              tot = x1+x2+x3+x4+x5
              gt.set(tot)
              
              Per = ((x1+x2+x3+x4+x5) * 100)/500
              per.set(Per)


              cg = (((x1+x2+x3+x4+x5) * 100)/500) / 9.5
              cgpa.set(round(cg,1))

              if cg > 10:
                     cgpa.set(10)


              if (((x1+x2+x3+x4+x5) * 100)/500) <= 40:
                     grd = 'G'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 50:
                     grd = 'F'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 60:
                     grd = 'E'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 70:
                     grd = 'D'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 80:
                     grd = 'C'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 90:
                     grd = 'B'
              else:
                     grd = 'A'

              grade.set(grd)

              count = 0
              if x1 < 33:
                     count = count + 1
              if x2 < 33:
                     count = count + 1
              if x3 < 33:
                     count = count + 1
              if x4 < 33:
                     count = count + 1
              if x5 < 33:
                     count = count + 1

              if (count == 0):
                     result.set('PASS')
              elif (count == 1 or count == 2 ):
                     result.set('SUPPLY')
              else:
                     result.set('FAIL')

              if Per <= 45 and result != "FAIL":
                     div.set('THIRD')
              elif Per <= 60 and result != "FAIL":
                     div.set('SECOND')
              elif Per <= 100:
                     div.set('FIRST')     

       def Reset():
              name.set(' ')
              roll.set(' ')
              fname.set(' ')
              mname.set(' ')
              DOB.set(' ')
              gender.set(' ')
              scl.set(' ')
              email.set(' ')
              m1.set(' ')
              m2.set(' ')
              m3.set(' ')
              m4.set(' ')
              m5.set(' ')
              gt.set(' ')
              per.set(' ')
              cgpa.set(' ')
              grade.set(' ')
              div.set(' ')
              result.set(' ')  
       

       #========================================================Frame_1===============================================================
       
       Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)


       #=================================================Labels and Entries for Frame_1===============================================
       Label_Name = Label(Frame_1, text = 'Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Name.grid(row = 0, column = 0, padx = 80)
       Entry_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = name)
       Entry_Name.grid(row = 0, column = 1, padx = 5, pady = 5)

       Label_Roll_no = Label(Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Roll_no.grid(row = 0, column = 3, padx = 80)
       Entry_Roll_no = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = roll)
       Entry_Roll_no.grid(row = 0, column = 4, padx = 40)

       Label_Father_Name = Label(Frame_1, text = 'Father Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Father_Name.grid(row = 1, column = 0, padx = 80)
       Entry_Father_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = fname)
       Entry_Father_Name.grid(row = 1, column = 1, padx = 5, pady = 10)

       Label_Mother_Name = Label(Frame_1, text = 'Mother Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Mother_Name.grid(row = 1, column = 3, padx = 80)
       Entry_Mother_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = mname)
       Entry_Mother_Name.grid(row = 1, column = 4, padx = 5)

       Label_DOB = Label(Frame_1, text = 'Date of Birth', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_DOB.grid(row = 2, column = 0, padx = 80)
       Entry_DOB = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = DOB)
       Entry_DOB.grid(row = 2, column = 1, padx = 5, pady = 5)

       Label_Gender = Label(Frame_1, text = 'Gender', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Gender.grid(row = 2, column = 3, padx = 80)
       Entry_Gender = ttk.Combobox(Frame_1, values = (' ','Male','Female','Others'), font = ('arial',15), width = 23, textvariable = gender)
       Entry_Gender.grid(row = 2, column = 4, padx = 5, pady = 5)


       Label_School = Label(Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_School.grid(row = 3, column = 0, padx = 80)
       Entry_School = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = scl)
       Entry_School.grid(row = 3, column = 1, padx = 5, pady = 5)

       Label_Email = Label(Frame_1, text = 'Email ID', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Email.grid(row = 3, column = 3, padx = 80)
       Entry_Email = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = email)
       Entry_Email.grid(row = 3, column = 4, padx = 5, pady = 5)



       #========================================================Frame_2==================================================================       
       Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10 \
                            , text = 'Grades Point Obtained', relief = 'ridge')
       Frame_2.grid(row = 3, column = 0)



       #======================================================Labels of Frame_2===========================================================

       Label_Subject = Label(Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 0, padx = 50, pady = 10)

       Label_obt_Marks = Label(Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 1, padx = 20)

       Label_Subject = Label(Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 2, padx = 20)

       Label_obt_Marks = Label(Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 3, padx = 20)

       Label_1 = Label(Frame_2, text = 'MATHEMATICS', font = ('arial',14), bg = 'Navajo white')
       Label_1.grid(row = 4, column = 0)
       Label_2 = Label(Frame_2, text = 'PHYSICS', font = ('arial',14), bg = 'Navajo white')
       Label_2.grid(row = 5, column = 0)
       Label_3 = Label(Frame_2, text = 'CHEMISTRY', font = ('arial',14), bg = 'Navajo white')
       Label_3.grid(row = 6, column = 0)
       Label_4 = Label(Frame_2, text = 'HINDI', font = ('arial',14), bg = 'Navajo white')
       Label_4.grid(row = 7, column = 0)
       Label_5 = Label(Frame_2, text = 'ENGLISH', font = ('arial',14), bg = 'Navajo white')
       Label_5.grid(row = 8, column = 0)
       Label_6 = Label(Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = 'Navajo white')
       Label_6.grid(row = 9, column = 0)
       Label_7 = Label(Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_7.grid(row = 10, column = 0)
       Label_8 = Label(Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_8.grid(row = 10, column = 2)
       Label_9 = Label(Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_9.grid(row = 10, column = 4)
       Label_10 = Label(Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 0)
       Label_10 = Label(Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 2)
       
       #======================================================Entries of Frame_2===========================================================
       var_1 = StringVar(Frame_2, value = '33')
       var_2 = StringVar(Frame_2, value = '100')
       var_3 = StringVar(Frame_2, value = '500')

       Entry__1 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m1)
       Entry__1.grid(row = 4, column = 1)
       Entry__2 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m2)
       Entry__2.grid(row = 5, column = 1)
       Entry__3 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m3)
       Entry__3.grid(row = 6, column = 1)
       Entry__4 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m4)
       Entry__4.grid(row = 7, column = 1)
       Entry__5 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m5)
       Entry__5.grid(row = 8, column = 1)
       Entry__6 = Entry(Frame_2, font = ('arial',14), width = 5, textvariable = gt, state = 'readonly')
       Entry__6.grid(row = 9, column = 1, pady = 8)
       Entry__7 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = per, state = 'readonly')
       Entry__7.grid(row = 10, column = 1, pady = 8)
       Entry__8 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa, state = 'readonly')
       Entry__8.grid(row = 10, column = 3, pady = 8)
       Entry__9 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade, state = 'readonly')
       Entry__9.grid(row = 10, column = 5, padx = 20, pady = 8)
       Entry__10 = Entry(Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = div, state = 'readonly')
       Entry__10.grid(row = 11, column = 1, padx = 20, pady = 8)
       Entry__11 = Entry(Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result, state = 'readonly')
       Entry__11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Entry_1_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Entry_1_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_1_3.grid(row = 4, column = 3)
       Entry_2_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Entry_2_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_2_3.grid(row = 5, column = 3)
       Entry_3_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Entry_3_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_3_3.grid(row = 6, column = 3)
       Entry_4_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Entry_4_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_4_3.grid(row = 7, column = 3)
       Entry_5_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Entry_5_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_5_3.grid(row = 8, column = 3)
       Entry_6_3 = Entry(Frame_2, textvariable = var_3, font = ('arial',16), width = 5, state = 'readonly')
       Entry_6_3.grid(row = 9, column = 3)
                


       #======================================================Buttons===========================================================
       Btn_Compute = Button(Frame_2, text = 'COMPUTE', font = ('arial',12,'bold'), width = 10, command = Compute)
       Btn_Compute.grid(row = 4, column = 4, padx = 50, pady = 6)
       Btn_Save = Button(Frame_2, text = 'SAVE', font = ('arial',12,'bold'), width = 10, command = Add)
       Btn_Save.grid(row = 5, column = 4, padx = 50, pady = 6)
       Btn_Update = Button(Frame_2, text = 'UPDATE', font = ('arial',12,'bold'), width = 10, command = Update)
       Btn_Update.grid(row = 6, column = 4, padx = 50, pady = 6)
       Btn_Cancel = Button(Frame_2, text = 'RESET', font = ('arial',12,'bold'), width = 10, command = Reset)
       Btn_Cancel.grid(row = 7, column = 4, padx = 50, pady = 6)
       Btn_Exit = Button(Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command = Exit)
       Btn_Exit.grid(row = 8, column = 4, padx = 50, pady = 6)


       root.mainloop()


def search_result_marksheet(row):
       root = Tk()
       root.title('Marksheet')
       root.geometry('1350x750')
       root.config(bg = 'Navajo white')

       
       #==============================================Functions==========================================================             
       
       def Compute():
              x1 = (m1.get());      x2 = (m2.get());    x3 = (m3.get());      x4 = (m4.get());    x5 = (m5.get())                                   
       
              tot = x1+x2+x3+x4+x5
              gt.set(tot)
              
              Per = ((x1+x2+x3+x4+x5) * 100)/500
              per.set(Per)


              cg = (((x1+x2+x3+x4+x5) * 100)/500) / 9.5
              cgpa.set(round(cg,1))


              if (((x1+x2+x3+x4+x5) * 100)/500) <= 40:
                     grd = 'G'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 50:
                     grd = 'F'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 60:
                     grd = 'E'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 70:
                     grd = 'D'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 80:
                     grd = 'C'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 90:
                     grd = 'B'
              else:
                     grd = 'A'

              grade.set(grd)

              count = 0
              if x1 < 33:
                     count = count + 1
              if x2 < 33:
                     count = count + 1
              if x3 < 33:
                     count = count + 1
              if x4 < 33:
                     count = count + 1
              if x5 < 33:
                     count = count + 1

              if (count == 0):
                     result.set('PASS')
              elif (count == 1 or count == 2 ):
                     result.set('SUPPLY')
              else:
                     result.set('FAIL')

              if Per <= 45 and result != "FAIL":
                     div.set('THIRD')
              elif Per <= 60 and result != "FAIL":
                     div.set('SECOND')
              elif Per <= 100:
                     div.set('FIRST')     

       
       

       #========================================================Frame_1===============================================================
       
       Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)

       name = StringVar(Frame_1,value=row[0][1])
       roll = StringVar(Frame_1,value=row[0][2])
       fname = StringVar(Frame_1,value=row[0][3])
       mname = StringVar(Frame_1,value=row[0][4])
       DOB = StringVar(Frame_1,value=row[0][5])
       gender = StringVar(Frame_1,value=row[0][6])
       scl = StringVar(Frame_1,value=row[0][7])
       email = StringVar(Frame_1,value=row[0][8])
       


       #=================================================Labels and Entries for Frame_1===============================================
       Label_Name = Label(Frame_1, text = 'Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Name.grid(row = 0, column = 0, padx = 80)
       Entry_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = name)
       Entry_Name.grid(row = 0, column = 1, padx = 5, pady = 5)

       Label_Roll_no = Label(Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Roll_no.grid(row = 0, column = 3, padx = 80)
       Entry_Roll_no = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = roll)
       Entry_Roll_no.grid(row = 0, column = 4, padx = 40)

       Label_Father_Name = Label(Frame_1, text = 'Father Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Father_Name.grid(row = 1, column = 0, padx = 80)
       Entry_Father_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = fname)
       Entry_Father_Name.grid(row = 1, column = 1, padx = 5, pady = 10)

       Label_Mother_Name = Label(Frame_1, text = 'Mother Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Mother_Name.grid(row = 1, column = 3, padx = 80)
       Entry_Mother_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = mname)
       Entry_Mother_Name.grid(row = 1, column = 4, padx = 5)

       Label_DOB = Label(Frame_1, text = 'Date of Birth', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_DOB.grid(row = 2, column = 0, padx = 80)
       Entry_DOB = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = DOB)
       Entry_DOB.grid(row = 2, column = 1, padx = 5, pady = 5)

       Label_Gender = Label(Frame_1, text = 'Gender', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Gender.grid(row = 2, column = 3, padx = 80)
       Entry_Gender = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = gender)
       Entry_Gender.grid(row = 2, column = 4, padx = 5, pady = 5)


       Label_School = Label(Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_School.grid(row = 3, column = 0, padx = 80)
       Entry_School = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = scl)
       Entry_School.grid(row = 3, column = 1, padx = 5, pady = 5)

       Label_Email = Label(Frame_1, text = 'Email ID', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Email.grid(row = 3, column = 3, padx = 80)
       Entry_Email = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = email)
       Entry_Email.grid(row = 3, column = 4, padx = 5, pady = 5)



       #========================================================Frame_2==================================================================       
       Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10 \
                            , text = 'Grades Point Obtained', relief = 'ridge')
       Frame_2.grid(row = 3, column = 0)

       m1 = DoubleVar(Frame_2,row[0][9])
       m2 = DoubleVar(Frame_2,row[0][10])
       m3 = DoubleVar(Frame_2,row[0][11])
       m4 = DoubleVar(Frame_2,row[0][12])
       m5 = DoubleVar(Frame_2,row[0][13])
       gt = DoubleVar(Frame_2,row[0][14])
       per = DoubleVar(Frame_2,row[0][15])
       cgpa = DoubleVar(Frame_2,row[0][16])
       grade = StringVar(Frame_2,row[0][17])
       div = StringVar(Frame_2,row[0][18])
       result = StringVar(Frame_2,row[0][19])

       #======================================================Labels of Frame_2===========================================================

       Label_Subject = Label(Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 0, padx = 50, pady = 10)

       Label_obt_Marks = Label(Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 1, padx = 20)

       Label_Subject = Label(Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 2, padx = 20)

       Label_obt_Marks = Label(Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 3, padx = 20)

       Label_1 = Label(Frame_2, text = 'MATHEMATICS', font = ('arial',14), bg = 'Navajo white')
       Label_1.grid(row = 4, column = 0)
       Label_2 = Label(Frame_2, text = 'PHYSICS', font = ('arial',14), bg = 'Navajo white')
       Label_2.grid(row = 5, column = 0)
       Label_3 = Label(Frame_2, text = 'CHEMISTRY', font = ('arial',14), bg = 'Navajo white')
       Label_3.grid(row = 6, column = 0)
       Label_4 = Label(Frame_2, text = 'HINDI', font = ('arial',14), bg = 'Navajo white')
       Label_4.grid(row = 7, column = 0)
       Label_5 = Label(Frame_2, text = 'ENGLISH', font = ('arial',14), bg = 'Navajo white')
       Label_5.grid(row = 8, column = 0)
       Label_6 = Label(Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = 'Navajo white')
       Label_6.grid(row = 9, column = 0)
       Label_7 = Label(Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_7.grid(row = 10, column = 0)
       Label_8 = Label(Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_8.grid(row = 10, column = 2)
       Label_9 = Label(Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_9.grid(row = 10, column = 4)
       Label_10 = Label(Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 0)
       Label_10 = Label(Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 2)
       
       #======================================================Entries of Frame_2===========================================================
       var_1 = StringVar(Frame_2, value = '33')
       var_2 = StringVar(Frame_2, value = '100')
       var_3 = StringVar(Frame_2, value = '500')

       Entry__1 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m1)
       Entry__1.grid(row = 4, column = 1)
       Entry__2 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m2)
       Entry__2.grid(row = 5, column = 1)
       Entry__3 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m3)
       Entry__3.grid(row = 6, column = 1)
       Entry__4 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m4)
       Entry__4.grid(row = 7, column = 1)
       Entry__5 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m5)
       Entry__5.grid(row = 8, column = 1)
       Entry__6 = Entry(Frame_2, font = ('arial',14), width = 5, textvariable = gt)
       Entry__6.grid(row = 9, column = 1, pady = 8)
       Entry__7 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = per)
       Entry__7.grid(row = 10, column = 1, pady = 8)
       Entry__8 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa)
       Entry__8.grid(row = 10, column = 3, pady = 8)
       Entry__9 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade)
       Entry__9.grid(row = 10, column = 5, padx = 20, pady = 8)
       Entry__10 = Entry(Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = div)
       Entry__10.grid(row = 11, column = 1, padx = 20, pady = 8)
       Entry__11 = Entry(Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result)
       Entry__11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Entry_1_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Entry_1_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_1_3.grid(row = 4, column = 3)
       Entry_2_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Entry_2_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_2_3.grid(row = 5, column = 3)
       Entry_3_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Entry_3_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_3_3.grid(row = 6, column = 3)
       Entry_4_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Entry_4_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_4_3.grid(row = 7, column = 3)
       Entry_5_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Entry_5_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_5_3.grid(row = 8, column = 3)
       Entry_6_3 = Entry(Frame_2, textvariable = var_3, font = ('arial',16), width = 5)
       Entry_6_3.grid(row = 9, column = 3)
                


       #======================================================Buttons===========================================================
       
       Btn_Exit = Button(Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command = root.destroy)
       Btn_Exit.grid(row = 8, column = 4, padx = 50, pady = 6)

       
       root.mainloop()

if __name__ == '__main__':
       marksheet()
