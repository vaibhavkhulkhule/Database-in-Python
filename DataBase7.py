'''
Function Name    :  Accept eno And Display All Info From Database Using GUI
Function Date    :  27 June 2021
Function Author  :  Prasad Dangare
Input            :  eno
Output           :  Display Employee Info

'''

import MySQLdb
from tkinter import*

root = Tk()

def Get_rows(eno):
    
    Connection = MySQLdb.connect(host = "localhost", database = "pythondb", user = "root", password = "-----")

    cobj = Connection.cursor()
    
    str = "select * from emptab where eno = '%d' "
    
    value = (eno)
    
    cobj.execute(str % value)
    
    row = cobj.fetchone()
    
    if row != None:
        lbl = Label(text = row, font = ('Arial', 14)).place(x = 50, y = 200)
    
    cobj.close()
    Connection.close()

def Display(self):
    
    str = Ent.get()
    
    lbl = Label(text = "You Entered : " + str, font = ('Arial', 14)).place(x = 50, y = 150)
    
    Get_rows(int(str))

frm = Frame(root, height = 350, width = 600)

frm.propagate(0)

frm.pack()

L1 = Label(text = "Enter Employee Number : ", font = ('Arial', 14))

Ent = Entry(frm, width = 15, fg = 'red', bg = 'yellow', font = ('Arial', 14))

Ent.bind("<Return>", Display)

L1.place(x = 50, y = 100)
Ent.place(x = 300, y = 100)

root.mainloop()
