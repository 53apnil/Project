import os.path
from os import path

def FileData_write(OutputFile, data, RecordList, FilePath):

    OutputFile.write("\n\n")
    OutputFile.write((FilePath.split("/"))[1])
    OutputFile.write("\n\n")
    for val in RecordList:
        OutputFile.write(val)
        OutputFile.write(" ")

    OutputFile.write("\n\n")

    data.seek(0, os.SEEK_SET)

    for line in data:

        if line.find("<tr>") != -1:
            index = line.rfind("<a href=")
            if index != -1:
                index += 8
                while(line[index] != ">"):
                    OutputFile.write(line[index])
                    index += 1
                OutputFile.write("\n")



def FileOpen(FilePath, HtmlFile):
    
    RecordList = list()

    filedata = list()
    #file OutputFile = open("OutputFile", "a")
    path = FilePath +"/"+ HtmlFile
    data = open(path, 'r')

    for line in data:

        if line.find("TOTAL</th>") != -1:
            index = line.find("TOTAL</th>")
            index += 31
            n = 0
            while n < 8:
                word = ""
                while line[index] != "<":
                    word = word + line[index]
                    index += 1
                index += 26
                n += 1
                RecordList.append(word)

    if((RecordList[1])[-1:] == 'k'):
        DataUse =  (RecordList[1])[ :-1]
        
        if float(DataUse) < 100:
            OutputFile  = open("KB_0_100","a")
            FileData_write(OutputFile, data, RecordList, FilePath)

        elif float(DataUse) >= 100 and float(DataUse) < 200:
                OutputFile = open("KB_100_200","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

        elif float(DataUse) >= 200 and float(DataUse) < 300:
                OutputFile = open("KB_200_300","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

        elif float(DataUse) >= 300 and float(DataUse) < 400:
                OutputFile = open("KB_300_400","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

        elif float(DataUse) >= 400 and float(DataUse) < 500:
                OutputFile = open("KB_400_500","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

        elif float(DataUse) >= 600 and float(DataUse) < 700:
                OutputFile = open("KB_600_700","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

        elif float(DataUse) >= 700 and float(DataUse) < 800:
                OutputFile = open("KB_700_800","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

        elif float(DataUse) >= 900 and float(DataUse) < 999:
                OutputFile = open("KB_100_200","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

    elif((RecordList[1])[-1:] == 'M'):
            DataUse = (RecordList[1])[:-1]

            if float(DataUse) < 100:
                OutputFile  = open("MB_0_100","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 100 and float(DataUse) < 200:
                    OutputFile = open("MB_100_200","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 200 and float(DataUse) < 300:
                OutputFile = open("MB_200_300","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 300 and float(DataUse) < 400:
                    OutputFile = open("MB_300_400","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 400 and float(DataUse) < 500:
                    OutputFile = open("MB_400_500","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 600 and float(DataUse) < 700:
                    OutputFile = open("MB_600_700","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 700 and float(DataUse) < 800:
                    OutputFile = open("MB_700_800","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 900 and float(DataUse) < 999:
                    OutputFile = open("MB_100_200","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

    else:
        if((RecordList[1])[-1:] == 'G'):
            DataUse = (RecordList[1])[:-1]

            if float(DataUse) < 1:
                OutputFile  = open("GB_1","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 1 and float(DataUse) < 2:
                    OutputFile = open("GB_1_2","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 2 and float(DataUse) < 4:
                OutputFile = open("GB_2_4","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 6 and float(DataUse) < 8:
                    OutputFile = open("GB_6_8","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)
            
            elif float(DataUse) >= 8 and float(DataUse) < 10:
                    OutputFile = open("GB_8_10","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 10 and float(DataUse) < 20:
                OutputFile = open("GB_10_20","a")
                FileData_write(OutputFile, data, RecordList, FilePath)

            elif float(DataUse) >= 20 and float(DataUse) < 40:
                    OutputFile = open("GB_20_40","a")
                    FileData_write(OutputFile, data, RecordList, FilePath)


def DirectoryFolder(User):

    for users in User:
        UserHtmlFile = (users.split('/'))[1]
        files = os.listdir(users)
    
        for htmlFile in files:
            htmlFiles = UserHtmlFile + ".html"
            if htmlFile == htmlFiles:
                FileOpen(users, htmlFiles)
                
def main_function():
    
    f_list = []
    d_list = list()

    DirectoryPath = "2019Sep08-2019Sep14"
    files = os.listdir(DirectoryPath)

    for directory in files: 
        if os.path.isfile(DirectoryPath +"/"+ directory) != True:
            d_list.append(DirectoryPath +"/"+ directory)

    DirectoryFolder(d_list)

#if __name__ == "__main__":
#        main()
