import re, os, codecs
os.chdir(r'/Data')

# 열기
f = open('friends.txt', 'r', encoding = 'utf8')
script101 = f.read()

# 연습해보기
print(script101[:100])
Line = re.findall(r'Monica:.+', script101)
print(Line[:3])
Line = re.findall(r'Monica:.+', script101)

# monica.txt 파일 만들기
f = open('monica.txt', 'w', encoding = 'utf8')
monica = '' # 빈 문자열을 저장하면 문자열 형식으로 객체가 만들어짐
for i in Line:
    monica += i + '\n'
f.write(monica)
f.close()

# 확인 하기
monica[:100]

f = open('monica.txt', 'w', encoding = 'utf8')
f.write(monica)
f.close

# 등장인물의 이름 모두 모으기
## 정규표현식 쓰기
char = re.compile(r'[A-Z][a-z]+:')

## 해당 식 찾아보기 (re.findall)
re.findall(char, script101)

## 중복된 값 제거하기, 예제
a = [1, 2, 3, 4, 5, 5, 3, 2]
set(a)

set(re.findall(char, script101))

## 등장인물이 아닌 것들(All과 같은 것)은 예외로 할 것
## 콜론 뺼 것
rachel = 'Rachel:'
rachel = re.sub(':', '', 'Rachel')
rachel

rachel[:-1]

# 문자열 슬라이싱을 이용해 앞에서 만든 리스트 요소에서 맨 뒤의 콜론(:)을 전부 지울 것
## 등장인물 리스트를 집합으로 바꿔 y 객체에 저장
y = set(re.findall(char, script101))

## for 문에 사용하기 위해 다시 리스트로 바꿈
x = list(y)

## 등장인물 리스트를 새로 담을 객체 character를 만듬
character = []
## 맨 뒤 콜론을 지우고 character에 저장
for i in x:
    character += [i[:-1]]

## character 리스트 확인하기
print(character)

character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
character

# 괄호 안에 있는 것들은 제거하기
## 정규표현식 구하기
print(script101)
re.findall(r'\([A-Za-z].+[A-Za-z]\)', script101)

# 특정 단어의 예문만 모아서 파일로 저장하기
f = open('friends.txt', 'r', encoding= 'utf8')
f.read(100)
f.seek(0) # 읽은 다음 커서를 맨 앞으로 가져감

# sentence 변수를 만들고 모든 문장을 원소로 저장하기
sentences = f.readlines()
sentences[:3]

# '사람이름: 대사' 패턴의 문자열 나오는 규칙 가진 문장 찾기
for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)

lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
lines[:10]

# would가 들어간 대사 찾아서 넣기
would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
would[:10]

# take가 들어간 문장
take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]
take

# writelines 사용하기
newf = open('would.txt', 'w', encoding='utf-8')
newf.writelines(would)
newf.close()

## 연습문제
words = ['apple', 'cat', 'brave', 'drama', 'arise', 'blow', 'coat', 'above']
for i in words:
    m = re.match(r'a\D+', i)
    if m:
        print(m.group())

a = '제 이메일 주소는 greatking@naver.com입니다. 오늘 저는 travel@daum.net 라는 주소로 메일을 보내려고 합니다. 저는 apple@gmail.com, life@abc.co.kr 라는 메일도 사용하고 있습니다.'
b = re.findall(r'[a-z]+@[A-Za-z0-9.]+', a)
b

exam = '저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2020년입니다.'
re.findall(r'\d.+?년', exam)

d = 'I have a dog. I am not a girl. You are not alone. I am happy.'
re.split(r'[.?]',d)

## 1) [A-Za-z] 2) set