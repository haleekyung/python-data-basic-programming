import csv, os

def OpenCsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output

def WriteCsv(filename, the_list):
    with open(filename, 'w', newline='') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)

def switch(listNmae):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', ' ', j))
            except:
                pass
    return listName

