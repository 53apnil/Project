def Count_Visit_Sites(filedata):

    data = dict()
    totalSites = open("TotalSited6","w")

    for line in filedata:
        if line in data.keys():
            data[line] = data[line] + 1
        else:
            data.update({line:1})

    for item in data:
        totalSites.write(item)

def main():
    try:
        fp = open("UesData4","r")
        Count_Visit_Sites(fp)
    except FileNotFoundError:
        print("File not found....!")
        return

if __name__ == "__main__":
    main()
