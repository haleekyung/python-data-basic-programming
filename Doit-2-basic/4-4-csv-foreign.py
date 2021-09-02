import os, re
import usecsv

os.chdir(r'/Users/leekyungha/PycharmProjects/python-data-basic-programming/Data')

# 파일 열기
total = usecsv.opencsv('popSeoul.csv')

# 콤마 등을 제거하는 함수 usecsv.switch를 사용합니다.
newPop = usecsv.switch(total)
# 4번째 구까지만 시험으로 출력해봅니다.
print(newPop[:4])

for i in newPop:
	foreign = 0
## 한 번 루프가 돌고 나면 foreign을 다시 지정해주어야 하므로 foreign을 0으로 먼저 지정합니다
	try:
		foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
		print(i[0], foreign)
## i[0]에는 지역구 이름이 저장되어 있고, foreign은 공식대로 우리가 계산한 외국인 비율입니다
	except:
		pass
new = [['구', '한국인', '외국인', '외국인 비율(%)']]
# 등록외국인의 비율이 3이 넘을 때만 넘을 때만 출력합니다.
for i in newPop:
        foreign = 0
        try:
            foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
            if foreign > 3:
                new.append([i[0], i[1],i[2],foreign])
        except:
            pass

# 3% 넘는 구만 파일로 저장하기
usecsv.writecsv('newPop.csv',new)