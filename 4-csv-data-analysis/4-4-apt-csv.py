import os, re, csv
os.chdir(r'/Data')

# 모듈
def opencsv(filename):
    f = open(filename, 'r', encoding='utf-8-sig')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output

def writecsv(filename, the_list):
    with open(filename, 'w', newline='') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return listName

apt = switch(opencsv('apt_201910.csv'))

apt[:3]
len(apt)

# 슬라이싱으로 원하는 자료 출력하기
apt[0]
for i in apt[:6]:
    print(i[0])

# 시군구, 아파트 단지명, 거래금액(만원) 출력해보기

for i in apt[:6]:
    print(i[0], i[4], i[8])

# 강원도에 120m2 이상 3억원 이하 아파트 검색하기
# 1) 강원도 글자 들어간 것만 찾기
# 2) 120m2 이상인 것 찾기
# 3) 3억원 이하인 것 찾기

new_list  = []

for i in apt:
    try:
        if re.match('강원', i[0]) and i[5] >= 120 and i[-4] <= 30000:
            new_list.append([i[0], i[4], i[-4]])
    except:
        pass

print(new_list)
writecsv('apt_120-30000.csv', new_list)