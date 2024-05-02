'''
Function Name    :  Display All Rows From Employee Table
Function Date    :  27 June 2021
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  It Display All Records Of Emptab

'''

# Here I Use MySQL Workbench / MySQL 8.0 Command Line Client

import MySQLdb
from MySQLdb.cursors import Cursor

def Connection():
    
    Connection = MySQLdb.connect(host = "localhost", database = "pythondb", user = "root", password = "-----")

    cobj = Connection.cursor()
    cobj.execute("select * from emptab")

    '''row = cobj.fetchone()
                                  OR
    while row != None:
        print(row)
        row = cobj.fetchone()'''

    rows = cobj.fetchall()
    
    print("Total Number of Rows are : ", cobj.rowcount)

    for row in rows:
        print(row)

    cobj.close()
    Connection.close()

def main():
    
    Connection()

if __name__ == "__main__":
    main()
