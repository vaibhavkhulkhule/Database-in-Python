'''
Function Name    :  Delete A Record From emptab
Function Date    :  27 June 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Record Get Deleted From The Row

'''

import MySQLdb

def Delete_Rows(eno):

    Connction = MySQLdb.connect(host = "localhost", database = "pythondb", user = "root", password = "-----")

    cobj = Connction.cursor()

    str = "delete from emptab where eno = '%d' "

    value = (eno)

    try:

        cobj.execute(str % value)
        Connction.commit()
        
        print("Row Deleted...")

    except:

        Connction.rollback()
        print("Not Deleted")

    finally:

        cobj.close()
        Connction.close()

def main():

    iNo = int(input("Enter The Eno : "))

    Delete_Rows(iNo)

if __name__ == "__main__":
    main()

