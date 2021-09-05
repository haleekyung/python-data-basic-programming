### 부가가치세 계산하기
## 물건 가격이 5,000원이고, 부가가치세가 10%인 경우의 계산
a = 5000 * 1.1
print(a)

## 원래 가격을 계산할 때
b = 5500 / 1.1
print(b)

## 8,000원짜리 음식의 부가가치세는
c = 8000 / 1.1
print(round(c,1))

### lambda 함수
y = lambda x : x * 3
y(12)

add = lambda a, b : a + b
add(2, 3)


## 문자열 슬라이싱
littleprince = '''여섯 살 적 나는 '체험한 이야기'라는 제목의, 원시림에 관한 책에서 기막힌 그림 하나를 본 적이 있다. 맹수를 집어 삼키고 있는 보아뱀 그림이었다. 위의 그림은 그것을 옮겨 그린 것이다. 그 책에는 이렇게 씌어 있었다.
'보아뱀은 먹이를 씹지도 않고 통째로 집어삼킨다. 그리고는 꼼짝도 하지 못하고 여섯 달 동안 잠을 자면서 그것을 소화시킨다.' '''

# 슬라이싱
littleprince[:10] # 10번쨰 까지 글자만 불러오고 싶을 때

# 람다 이용하기
short_lp = lambda x : x[:10]
short_lp(littleprince)

## 람다를 이용해 환율 계산하기
exchange = lambda won : won * 0.00086
exchange(10000)
exchange(800000)

### def문 사용하기
## def문을 이용해 계산기 만들기
## 사칙연산 모두 수행하는 새로운 함수 calculator() 만들기

def calculator(a, b):
    return a + b, a - b, a * b, a / b

calculator(12, 3)
type(calculator(12, 3))

## 홀짝 구분하기, input()함수 사용하기
def seperate():
    a = int(input("자연수 중 하나를 입력하세요: "))
    if a % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")

seperate()


### 파이썬 비교연산자 이용
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i % 2 != 0:
        print(i, "홀수")
    else:
        print(i, "짝수")


### 서비스 가격 출력 프로그램 만들기
def service_price():
    service = input("서비스 종류를 입력하세요 (a/b/c): ")
    value = input("부가세 포함 여부를 입력하세요 (y/n): ")
    if value == "y":
        if service == "a":
            result = 23 * 1.1
        if service == "b":
            result = 40 * 1.1
        if service == "c":
            result = 67 * 1.1
    if value == "n":
        if service == "a":
            result = 23
        if service == "b":
            result = 40
        if service == "c":
            result = 67

    print(result,'만 원 입니다.')

service_price()


### 연습문제
# 01.
# print(14 % 4)
# 답: 2
# ----------
# 02.
# round(1.12345, 2)
# >> 1.12
# ----------
# 03.
a = int(input("나이를 입력하시오: "))
print(40 - a)
# ----------
plus = lambda x, y : x + y
plus(34, 54)
# ----------
def mean(a, b):
    return (a + b) / 2

mean(33, 22)
45 + mean(33, 22)
# ----------
b = [1, 2, 3, 10, 11, 12]

for i in b:
    if i < 10:
        print(i)
    else:
        print(i - 10)