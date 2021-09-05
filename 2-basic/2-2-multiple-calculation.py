## 100 미만 7의 배수를 모두 구하고 싶을 때
for i in range(100):
    if i % 7 == 0:
        print(i)

## 평균 나이 구하기
# 50, 45, 33, 39, 29, 30살 그룹의 평균 나이를 구해보기
a = (50 + 45 + 33 + 39 + 29 + 30) / 6 # 또는
b = (50 + 45 + 33 + 39 + 29 + 30) // 6

print("평균 나이는 {}세 입니다".format(round(a, 1)))
print("평균 나이는 {}세 입니다".format(b))

# round 함수 사용하기
round(a, 1)

## 19단 곱셈식 만들기
for item in range(19):
    item += 1
    for each in range(19):
        each += 1
        print(item, 'X', each, '=', item * each)

# 문자열 포매팅으로 print()함수 사용하기
print('%d X %d = %d' %(item, each, item * each))

# 문자열 포매팅 연습
print("나는 사과 %d개와, 배 %d개를 먹었습니다." %(5, 4))