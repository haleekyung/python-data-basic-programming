## 2. 첫 번째 행에 컴퓨터, 노트북, 태블릿, 두 번째 행에 100, 80, 60이라는 값이 포함된 자료를 CSV형 리스트로 만들어 볼 것
stuff = [['컴퓨터', '노트북', '태블릿'],[100, 80, 60]]
print(stuff)

## 3. 1, 2에 들어갈 함수 구하가
## 문자형으로 저장된 숫자를 정수형을 바꾸려 할 때 어떻게 해야 하는가?

import re
total = ['종로구', '151,767', '11,093', '27,394']
for i in total:
    if re.search(',', i):
        total[total.index(i)] = int(re.sub(',', '', i))
print(total)

## 4. CSV향 리스트 pop을 다음과 같이 정의하였는데, 조건식의 부분을 바꾸어 오류를 수정하시오

pop = [['종로구', 151767.0], ['중구', 126409.0], ['용산구', 228830.0], ['광진구', 352692.0], ['동대문구', 346551.0]]

for i in pop:
    if i[1] < 300000:
        print(i[0], i[1])

