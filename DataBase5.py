'''
Function Name    :  Update A Record From emptab
Function Date    :  27 June 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Record Was Update Into The Table 

'''

import MySQLdb

def Update_Rows(eno):

    Connection = MySQLdb.connect(host = "localhost", database = "pythondb", user = "root", password = "-----")

    cobj = Connection.cursor()

    str = "update emptab set sal = sal + 500 where eno = '%d' "

    value = (eno)

    try:

        cobj.execute(str % value)
        Connection.commit()

        print("Row Updated...")

    except:

        Connection.rollback()
        print("Not Updated")

    finally:

        cobj.close()
        Connection.close()

def main():

    iNo = int(input("Enter The Eno : "))

    Update_Rows(iNo)

if __name__ == "__main__":
    main() 
