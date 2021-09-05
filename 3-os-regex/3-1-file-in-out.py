## os 모듈 임포트하기
import os

## 현재 위치 확인하기
os.getcwd()

## 폴더 이동하기
os.chdir()

## 폴더 안의 파일 확인하기
os.getcwd()

## 어떤 파일 있는지 확인하기
os.listdir()

## listdir() 안의 결과값을 모두 리스트로 만들기
# 해당 과정이 중요한 이유는 리스트화 시킨 모든 파일 중 일부를 한번에 다른 곳으로 이동시킬 수 있고, 삭제 또는 수정 등도 가능하기 때문
folderFile = os.listdir()
type(folderFile)
print(folderFile)

## 파일 열고 닫기
f = open('a.txt', 'w') # '쓰기 - w' 모드

open('a.txt', 'w').write('abc')
f.close() # 파일 닫기

## 파일 열기 모드 알아보기 : 'w' , 'r' , 'a'
f = open('a.txt', 'w')

f.write('나는 오늘 학교에 갔다.')
f.close()

f = open('a.txt', 'r')
f.read()

# seek : 커서 위치 찾기
f.seek(0) # 파일 가장 처음으로 커서를 이동해라,
f.read()
f.close()

# 실행 폴더에 없는 파일을 읽기 모드로 불러보기
f = open('b.txt', 'r') # 오류 난다.

f = open('a.txt', 'r')
diary = f.read()
print(diary)
print(diary[:5])
f.close()

# 파일 추가하기 할 때는 'a'를 쓴다.
f = open('a.txt', 'a')
f.write(' 학교에 가지 않을 날이 올까?')
f.close()
f = open('a.txt', 'r')
f.read()
f.close()

# 파일 닫기 번거로움 문제 해결
with open('abcde.txt', 'w') as f:
    f.write('오늘 나는 학교에 갔습니다.')

## 한글파일 오류 해결하기
f = open('한글파일.txt', 'w', encoding='utf8')
f = open('한글파일.txt', 'r', encoding='utf8')

# codecs 모듈로 해결하는 방법
import codecs
f = codecs.open('한글파일.txt', 'r', 'utf-8')
f.read()[:10]