import csv, os
os.chdir(r'/Users/leekyungha/PycharmProjects/python-data-basic-programming/Data')
f = open('a.csv', 'r', encoding='utf-8-sig')

# CSV에서 저장한 객체를 파이썬으로 읽으려면 csv.reader를 사용할 것
new = csv.reader(f)

# a.csv파일의 내용을 파이썬에서 사용할 수 있도록 CSV형 리스트로 바꿈
a_list = []
f.seek(0)
for i in new:
    print(i)
    a_list.append(i)

a_list

# 함수로 저장
def opencsv(filename):
    f = open(filename, 'r', encoding='utf-8-sig')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

opencsv('a.csv')

a = [['구', '전체', '내국인', '외국인'],
['관악구', '519864', '502089', '17775'],
['강남구', '547602', '542498', '5104'],
['송파구', '686181', '679247', '6934'],
['강동구', '428547', '424235', '4312']]

f = open('abc.csv', 'w', newline = '')
csvobject = csv.writer(f, delimiter = ',')
csvobject.writerows(a)
f.close()

def writecsv(filename, the_list):
     with open(filename, 'w', newline = '') as f:
     a = csv.writer(f, delimiter = ',')
     a.writerows(the_list)