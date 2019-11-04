def readFileInput(datafile):

    usedatafp = open("UesData4","w")
    redatafp = open("Notusedata5","w")

    for line in datafile:
        dotsplit = []
        dotsplit = line.split(".")
        redatafp.write(dotsplit[0])
        if(len(dotsplit)>= 2):
            usedatafp.write(dotsplit[1])
        usedatafp.write("\n")
        if(len(dotsplit) >= 3):
            for rem in range(2, len(dotsplit)):
                redatafp.write(dotsplit[rem])
        
def main():
    try:
        fp = open("OutputFile1","r")
        readFileInput(fp)
    except FileNotFoundError:
        print("File does not found")
        return


if __name__ == "__main__":
    main()
