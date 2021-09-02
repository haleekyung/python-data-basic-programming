import os, re
import usecsv

os.chdir(r'/Users/leekyungha/PycharmProjects/python-data-basic-programming/Data')

# 파일 열기
total = usecsv.opencsv('popSeoul.csv')

# 콤마 등을 제거하는 함수 usecsv.switch를 사용
newPop = usecsv.switch(total)

# 4번째 구까지만 시험으로 출력
print(newPop[:4])

# 외국인 등록 비율 테스트
i = newPop[1]
print(i)

cal = i[2] / (i[1] + i[2]) * 100
print(cal)

## 소수점 첫째자리까지만 저장할 것
cal = round(i[2] / (i[1] + i[2]) * 100, 1)
print(cal)

# 각 구의 외국인 비율 출력하기
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2] * 100, 1))
        print(i[0], foreign)

    except:
        pass

new = [['구', '한국인', '외국인', '외국인 비율(%)']]

new.append([i[0], i[1], i[2], foreign])
print(new)

# 외국인 비율이 3% 초과할 때만 출력해보기
import re

for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            print([i[0], i[1], i[2], foreign])
    except:
        pass

new = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append(i[0], i[1], i[2], foreign)

    except:
        pass

usecsv.writecsv('newPop.csv', new)