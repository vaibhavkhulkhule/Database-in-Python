'''
Function Name    :  Insert Multiple Records Into emptab
Function Date    :  27 June 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Record Get Inserted Into The Row

'''

from DataBase2 import Connection
import MySQLdb

def Insert_Rows(eno, ename, sal):

    Connection = MySQLdb.connect(host = "localhost", database = "pythondb", user = "root", password = "-----")

    cobj = Connection.cursor()

    str = "insert into emptab(eno, ename, sal) values ('%d', '%s', '%f')"

    values = (eno, ename, sal)

    try:

        cobj.execute(str % values)
        Connection.commit()
        print("Row Inserted")

    except:
        
        Connection.rollback()
        print("Not Inserted")

    finally:

        cobj.close()
        Connection.close()

def main():

    iNo = int(input("How Many Rows You Want : "))

    for i in range(iNo):

        Eno = int(input("Enter The ENO : "))
        Nam = input("Enter The Name : ")
        Sal = int(input("Enter The Salary : "))

        Insert_Rows(Eno, Nam, Sal)
        print("---------------")

if __name__ == "__main__":
    main()
