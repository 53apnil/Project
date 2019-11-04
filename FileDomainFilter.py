import os


def RemoveSpaceFile(myFile):

    myfile = myFile.split("/")
    print(myfile[1])
    fp0 = open(myfile[1], "r")
    myfiles = myfile[1] + "s"
    fp1 = open(myfiles, "w")
    print(myfile[1], myfiles)

    for line in fp0:
        #print(line)
        word = line.split(" ")
        for i in range(0, len(word)):
            if word[i] != " ":
                break
        for j in range(i, len(word)):
            if word[j] != "\n":
                fp1.write(word[j])
    os.remove(myfile[1])

def main():
    
    path = "Web sites files"
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)
        RemoveSpaceFile(f)


if __name__ == "__main__":
    main()
