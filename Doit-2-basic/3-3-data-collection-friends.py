import os, re
os.chdir(r'/Users/leekyungha/PycharmProjects/python-data-basic-programming/Data')

# 열기
f = open('friends.txt', 'r', encoding = 'utf8')
script101 = f.read()

# 연습해보기
print(script101[:100])

Line = re.findall(r'Monica:.+', script101)
print(Line[:3])

for item in Line[:3]:
    print(item)

f.close()

f = open('monica.txt', 'w', encoding = 'utf8')
monica = ''

for i in Line:
    monica += i

f.write(monica)
f.close