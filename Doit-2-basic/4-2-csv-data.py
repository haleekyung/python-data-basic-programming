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

