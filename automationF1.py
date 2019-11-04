import time
import datetime
import os

def Copy_File(fp1, fp2):

    print("\n\nCurrent Time is")
    print(datetime.datetime.now())
    pre_time = time.time()
    
    try:
        while True:
            line = fp2.readline()
            fp1.write(line)
            if((time.time() - pre_time) > 2 and (time.time() - pre_time) <= 3 ):
                fp1.close()
                print("Current file line no ", (fp2.tell()))
                if line is None:
                    return "EOF"
                return time.time()
    except EOFError :
        return "EOF"
