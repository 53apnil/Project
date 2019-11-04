import os.path
from os import path

def ConvertIntoMB(Value):
    if(Value[-1:] == 'K'):
        return ((float(Value[:-1]))/1000)
    if(Value[-1:] == 'G'):
        return ((float(Value[:-1]))*1000)
    if(Value[-1:] == 'M'):
        return(float(Value[:-1]))
    return float(Value)


def FilterSite(Site):
    if(Site.rfind("http://") != -1):
        return(Site[8:])
    return(Site)


def FileOpen(FilePath, HtmlFile, userFile):
    
    Username = FilePath.split("/")
    path = FilePath +"/"+ HtmlFile
    data = open(path, 'r')
    userFile.write("\n\n")
    userFile.write("User Name =  ")
    userFile.write(Username[1])
    userFile.write("\n\n")

    userData = dict()
    #print("\n\n\n")
    #print(path)
    for line in data:
        cnt = 0
        if line.find("<tr>") != -1:
            index = line.rfind("<a href=")
            if index != -1:
                index += 8
                col = ""
                while(line[index] != ">"):
                    col += line[index]
                    cnt = cnt + 1
                    index += 1
                splits = col.split(".")
                if(len(splits)>2):
                    site = splits[len(splits)-2]
                else:
                    site = splits[0]
                site = FilterSite(site)
                index += cnt - 9
                index += 27
                while(line[index] != "<"):
                    index += 1
                index += 22
                col = ""
                while(line[index] != "<"):
                    col += line[index]
                    index += 1
                value = col
                MB = ConvertIntoMB(value)
                if site in userData.keys():
                    userData[site] += MB
                else:
                    userData.update({site:MB})
    #print(userData)                    
    for key, value in userData.items():
        userFile.write("Sites = : ")
        userFile.write(key)
        userFile.write("\nData uses = : ")
        userFile.write(str(value))
        userFile.write(" MB")
        userFile.write("\n\n")


def DirecoryFolder(User, UserFile):

    for users in User:
        UserHtmlFile = (users.split('/'))[1]
        files = os.listdir(users)

        for htmlFile in files:
            htmlFiles = UserHtmlFile + ".html"
            if htmlFile == htmlFiles:
                FileOpen(users, htmlFiles, UserFile)

def main():

    d_list = []
    DirectoryPath = "2019Sep08-2019Sep14"
    files = os.listdir(DirectoryPath)
    userFile = open("UserFile9", "w")
    for directory in files:
        if os.path.isfile(DirectoryPath +"/"+ directory) != True:
            d_list.append(DirectoryPath +"/"+ directory)
    DirecoryFolder(d_list, userFile)
    userFile.close()
        
if __name__ == "__main__":
    main()
