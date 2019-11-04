from collections import Counter

def Count_Visit_Sites(filedata):

    data = dict()
    totalVisite = open("TotalVisite7","w")
    topVisite100 = open("TopVisites8","w")

    for line in filedata:
        if line in data.keys():
            data[line] = data[line] + 1
        else:
            data.update({line:1})

    count = 0
    for item in data:
        totalVisite.write("\n")
        totalVisite.write("sites : {}  count : {}".format(item,data[item]))
        count = count + data[item]
        totalVisite.write("\n")
    totalVisite.write("Total Count ={} ".format(count))

    k = Counter(data)
    heigh = k.most_common(100)
    for record in heigh:
        topVisite100.write("\nSites : ")
        topVisite100.write(record[0])
        topVisite100.write("::  Total Visite : ")
        topVisite100.write("{}".format(record[1]))
        topVisite100.write("\n")

def main():
    try:
        fp = open("UesData4","r")
        Count_Visit_Sites(fp)
    except FileNotFoundError:
        print("File not found....!")
        return


if __name__ == "__main__":
    main()
