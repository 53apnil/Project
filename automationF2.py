import os
import automationF1
import datetime
import time


def Run_Function(fp2):
    
    print("Run function work", datetime.datetime.now())
    print("File Copy start\n")
    fp1 = open("access.log", "a")
    n = automationF1.Copy_File(fp1, fp2)
    if n == "EOF":
        print("Waiting for some time to log file genrate....!\n")
        time.sleep(2)
    print("File Copy complete \n")

def Run_Sarg(): 
    
    print("Run Sarg work", datetime.datetime.now())
    os.system('sarg -x')
    print("sarg Complete work")

def Delete_Access1_File():

    print("Delete Access File work", datetime.datetime.now())
    os.remove("access.log")
    print("Sucessfully deleted")
    time.sleep(2)


def main():

    fp2 = open("access1.log", "r")
    while 1:
        Run_Function(fp2)
        Run_Sarg()
        print("Delete file")
        time.sleep(2)
        Delete_Access1_File()

        print("Acces file delete")


if __name__ == "__main__":
    main()
