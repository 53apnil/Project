import os.path
import MultiFileDataDistrubuted11
from os import path
from collections import Counter

def FileOpen(FilePath, HtmlFile):

    OutputFile = open("OutputFile1", "a")
    path = FilePath +"/"+ HtmlFile
    data = open(path, 'r')
    
    for line in data:
        if line.find("<tr>") != -1:
            index = line.rfind("<a href=")
            if index != -1:
                index += 8
                while(line[index] != ">"):
                    OutputFile.write(line[index])
                    index += 1
                OutputFile.write("\n")


def DirectoryFolder(User):

    for users in User:
        UserHtmlFile = (users.split('/'))[1]
        files = os.listdir(users)
    
        for htmlFile in files:
            htmlFiles = UserHtmlFile + ".html"
            if htmlFile == htmlFiles:
                FileOpen(users, htmlFiles)

def Create_Count_Sites():
    
    data = dict()

    filedata = open("OutputFile1", "r")
    filerecord = open("FileRecord2","a")
    toprecord = open("TopRecords3", "a")

    for line in filedata:
        if line in data.keys():
            data[line] = data[line] + 1
        else:
            data.update({line:0})
    
    count = 0
    for item in data:
        filerecord.write("\n")
        filerecord.write("sites : {}count : {}".format(item,data[item]))
        count = count + data[item]
        filerecord.write("\n")
    filerecord.write("Total Count ={} ".format(count))
    k = Counter(data)
    heigh = k.most_common(100)

    for record in heigh:
        toprecord.write("\nSites : ")
        toprecord.write(record[0])
        toprecord.write("::  Total Visite : ")
        toprecord.write("{}".format(record[1]))
        toprecord.write("\n")

def main():
    d_list = list()
    DirectoryPath = "2019Sep08-2019Sep14"
    files = os.listdir(DirectoryPath)

    for directory in files: 
        if os.path.isfile(DirectoryPath +"/"+ directory) != True:
            d_list.append(DirectoryPath +"/"+ directory)
    
    MultiFileDataDistrubuted11.main_function()
    DirectoryFolder(d_list)
    Create_Count_Sites()

if __name__ == "__main__":
        main()
