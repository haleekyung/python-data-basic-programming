import re
example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다 (Lion, 2018)'

result = re.findall(r'\([A-za-z가-힣]+, \d+\)', example)
result

# re.match(패턴, 문자열)
pattern = r'life'
script = 'life'

re.match(pattern, script).group()
re.match(r'life', 'life').group()
re.match(r'life', 'animal').group()

# 함수로 조건 만들기
def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print("Not a match!")

pattern =  r'Life' #대문자 인식함
script = 'Life is so cool'
refinder(pattern, script)

# match 함수는 문자역 시작부터 매치여부를 알아보는 함수이기 떄문에 처음에 매치 안되면 작동 안됨
pattern = r'is'
script = 'Life is so cool'
refinder(pattern, script)

# search
def search(pattern, script):
    if re.search(pattern, script):
        print('Match!')
    else:
        print("Not a match!")

pattern = r'is'
script = 'Life is so cool'
search(pattern, script)

# findall
number = 'My number is 511223-1****** and your number is 521012-2******'
re.findall('\d{6}', number)

# 정규표현식 탐욕 제어하기
example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
re.findall(r'\d.+년', example1) # .이 들어가서 다 나옴
re.findall(r'\d.+?년', example1) # ?를 넣었더니 제대로 나옴

example
result = re.findall(r'\(.+\)', example)
result

result = re.findall(r'\(.+?\)', example)
result

# split 메서드 - 문장이 .!?로 끝나는 패턴을 생각해서 자를 수 있다.
sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog'
re.split(r'[.!?]', sentence)

data = 'a:3; b:4; c:5'
for i in re.split(r';', data):
    print(re.split(r':', i))

# sub 메서드 : 문자열 바꾸기
re.sub(r'dog', 'cat', sentence)

# sub 메서드를 이용해 줄바꿈 줄이기
words = 'I am home now. \n\n\n I am with my cat. \n\n'
print(words)
re.sub(r'\n', '', words)

# 'ly'로 끝나는 단어 추출하기
re.findall(r'\w+ly', sentence)