from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import Fee_Backend


class Fee():
    def __init__(self, master):
        self.master = master
        self.master.title('Fee Report')
        self.master.geometry('1350x750')
        self.master.config(bg='Navajo white')

        # ==================================================Variables=================================================
        self.recpt = StringVar()
        self.name = StringVar()
        self.admsn = StringVar()
        self.date = StringVar()
        self.branch = StringVar()
        self.sem = StringVar()
        self.total = DoubleVar()
        self.paid = DoubleVar()
        self.due = DoubleVar()

        # ==================================================Functions=================================================
        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                self.admsn_entry.delete(0, END)
                self.admsn_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, st[5])
                self.sem_entry.delete(0, END)
                self.sem_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.due_entry.delete(0, END)
                self.due_entry.insert(END, st[9])
            except IndexError:
                pass

        def Insert():
            if (len(self.admsn.get()) != 0):
                Fee_Backend.insert(self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(),
                                   self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(),
                                   self.due.get())
                self.list.delete(0, END)
                self.list.insert(END, (self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(),
                                       self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(),
                                       self.due.get()))

        def View():
            self.list.delete(0, END)
            for row in Fee_Backend.view():
                self.list.insert(END, row, str(' '))

        def Reset():
            self.recpt.set(' ')
            self.name.set(' ')
            self.admsn.set(' ')
            #self.date.set(' ')
            self.branch.set(' ')
            self.sem.set(' ')
            self.paid.set(' ')
            self.due.set(' ')
            self.Display.delete('1.0', END)
            self.list.delete(0, END)

        def Delete():
            Fee_Backend.delete(st[0])
            Reset()
            View()

        def Receipt():
            self.Display.delete('1.0', END)
            self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
            self.Display.insert(
                END, '\tReceipt No.\t     :' + self.recpt.get() + '\n')
            self.Display.insert(END, '\tStudent Name  :' +
                                self.name.get() + '\n')
            self.Display.insert(END, '\tAdmission No.\t:' +
                                self.admsn.get() + '\n')
            self.Display.insert(
                END, '\tDate\t          :' + self.date.get() + '\n')
            self.Display.insert(
                END, '\tBranch\t          :' + self.branch.get() + '\n')
            self.Display.insert(
                END, '\tSemester \t        :' + self.sem.get() + '\n\n')

            x1 = (self.var_1.get())
            x2 = (self.paid.get())
            x3 = (x1 - x2)

            self.Display.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
            self.Display.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
            self.Display.insert(END, '\tBalance\t         :' + str(x3) + '\n')

            self.due.set(x3)

        def Search():
            self.list.delete(0, END)
            for row in Fee_Backend.search(self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(),
                                          self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(),
                                          self.due.get()):
                self.list.insert(END, row, str(' '))

        def Update():
            Fee_Backend.delete(st[0])
            Insert()

        def Exit():
            Exit = tkinter.messagebox.askyesno(
                'Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return

        # ==================================================Frames===================================================
        Main_Frame = Frame(self.master, bg='Navajo white')
        Main_Frame.grid()

        Title_Frame = LabelFrame(
            Main_Frame, width=1350, height=100, bg='Navajo white', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        self.lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), text='FEE REPORT',
                              bg='navajowhite', padx=13)
        self.lblTitle.grid(padx=400)

        Data_Frame = Frame(Main_Frame, width=1350, height=350,
                           bg='Navajo white', relief='ridge', bd=15)
        Data_Frame.pack(side=TOP, padx=15)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Informations', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10)

        Frame_2 = LabelFrame(Data_Frame, width=495, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Fee Receipt', font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT, padx=10)

        List_Frame = Frame(Main_Frame, width=1350, height=150,
                           bg='Navajo white', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15)

        Button_Frame = Frame(Main_Frame, width=1350, height=80,
                             bg='Navajo white', relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        # ===================================================Labels================================================
        self.recpt_label = Label(Frame_1, text='Receipt No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.recpt_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Student Name : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        self.admsn_label = Label(Frame_1, text='Admission No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.admsn_label.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_label = Label(Frame_1, text='Date : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.Date_label.grid(row=3, column=0, padx=15, sticky=W)

        self.branch_label = Label(Frame_1, text='Branch : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.branch_label.grid(row=4, column=0, padx=15, sticky=W)

        self.sem_label = Label(Frame_1, text='Semester : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.sem_label.grid(row=5, column=0, padx=15, sticky=W)

        self.total_label = Label(Frame_1, text='TOTAL AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.total_label.grid(row=2, column=2, padx=5, sticky=W)

        self.paid_label = Label(Frame_1, text='PAID AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.paid_label.grid(row=3, column=2, padx=5, sticky=W)

        self.due_label = Label(Frame_1, text='BALANCE : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.due_label.grid(row=4, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        self.var_1 = DoubleVar(Frame_1, value='36265')
        d1 = datetime.date.today()
        self.date.set(d1)

        self.recpt_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.recpt)
        self.recpt_entry.grid(row=0, column=1, padx=15, pady=5)

        self.name_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.name)
        self.name_entry.grid(row=1, column=1, padx=15, pady=5)

        self.admsn_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.admsn)
        self.admsn_entry.grid(row=2, column=1, padx=15, pady=5)

        self.Date_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.date)
        self.Date_entry.grid(row=3, column=1, padx=15, pady=5)

        self.branch_entry = ttk.Combobox(Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical', 'Civil', 'EE', 'EEE'),
                                         font=('arial', 14), width=19, textvariable=self.branch)
        self.branch_entry.grid(row=4, column=1, padx=15, pady=5)

        self.sem_entry = ttk.Combobox(Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH',
                                                       'SEVENTH', 'EIGHTH'), font=('arial', 14), width=19,
                                      textvariable=self.sem)
        self.sem_entry.grid(row=5, column=1, padx=15, pady=5)

        self.total_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_1, state='readonly')
        self.total_entry.grid(row=2, column=3, padx=8, pady=5)

        self.paid_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.paid)
        self.paid_entry.grid(row=3, column=3, pady=5)

        self.due_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.due)
        self.due_entry.grid(row=4, column=3, pady=7)

        # ==================================================Frame_2=================================================
        self.Display = Text(Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)

        # =============================================List box and scrollbar===========================================
        sb = Scrollbar(List_Frame)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(List_Frame, font=(
            'arial', 13, 'bold'), width=140, height=8)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)

        # ==================================================Buttons=================================================
        btnSave = Button(Button_Frame, text='SAVE', font=(
            'arial', 14, 'bold'), width=10, command=Insert)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text='DISPLAY', font=(
            'arial', 14, 'bold'), width=10, command=View)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='RESET', font=(
            'arial', 14, 'bold'), width=10, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10, command=Update)
        btnReset.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text='SEARCH', font=(
            'arial', 14, 'bold'), width=10, command=Search)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text='DELETE', font=(
            'arial', 14, 'bold'), width=10, command=Delete)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(Button_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'), width=10, command=Receipt)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)

        btnExit = Button(Button_Frame, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=Exit)
        btnExit.grid(row=0, column=7, padx=5, pady=5)


root = Tk()
obj = Fee(root)
root.mainloop()
