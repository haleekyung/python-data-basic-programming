import os, re
import usecsv # 모듈
os.chdir(r'/Users/leekyungha/PycharmProjects/python-data-basic-programming/Data')

total = usecsv.OpenCsv('popSeoul.csv')
print(total[:5])

for i in total[:5]:
    print(i)

# 문자형 자료를 숫자형으로 바꾸기 - ',' 제외하기
# sub 함수 사용하기

# 예제
i = '123'
print(float(i))
int(i)

b = '123,455,677'

# b 변수의 쉼표 삭제하기: sub 함수 사용하기
float(re.sub(',', '', b))

# 숫자 원소만 골라서 쉼표 제거하기
i = total[2]
print(i)

check_float = []
for j in i:
    if re.search('\d', j):
        check_float.append(float(re.sub(',', '', j)))

    else:
        check_float.append(j)

print(check_float)

# 문자와 숫자가 섞인 원소 골라내기
# '123강남'과 같이 문자와 숫자가 섞인 경우 위의 조건만 실행하게 되면, '123'이 있기 때문에 이것을 정수로 인식하게 되어 오류메세지 띄워짐
# 따라서 '123은 들어가지만 문자도 같이 들어가는 경우에는 이것을 str으로 인식하게 함'

dw = ['123강남', '151.340', '123,454', '10,333']
print(dw)
k = []
for i in dw:
    if re.search('[a-z가-힣]', dw):
        k.append(i)
    else:
        k.append(re.sub(float( ',', '', 'i')))

print(k)


# 특수문자와 숫자가 섞인 원소 골라내기
k = []
i = ['123!!', '151.340', '123,454', '10,333']
for j in i:
    if re.search('[a-z가-힣!]', j):
        k.append(j)
    else:
        k.append(float(re.sub(',', '', j)))


print(k)

# 첫번제 행을 인덱스로 저장하고 싶을 때
k = [ ]
i = [ '123!!', '151.340', '123,454', '10,333' ]
for j in i:
    if re.search( '[a-z가-힣!]', j ):
        i[i.index(j)] = j
    else:
        i[i.index(j)] = ( float( re.sub( ',', '', j ) ) )

print(i)

# 예외처리하기 - 빈 칸에 대한 대처는 예외처리로.
k = [ ]
i = [ '123!!', '151.340', '123,454', '10,333', '', '#$%^172737']
for j in i:
    try:
        i[i.index(j)] = ( float( re.sub( ',', '', j ) ) )
    except:
        pass

print(i)

# 예외처리하기 - 예외처리로 숫자만 골라서 숫자형으로 만들기
