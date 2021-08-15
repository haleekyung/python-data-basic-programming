## 왜 공부해야 하는가?
어떤 데이터 타입이냐에 따라, 메모리를 사용하는 범위가 달라질 수 있기 때문에 많은 메모리를 사용할 것을 대비하여 효율적인 데이터타입을 사용하는 것이 좋음.

메모리 낭비를 하지 않기 위해 바이트를 알맞게 사용함

## Binary digits
### bit : 0 또는 1과 같은 이진수
* 1 bit : 0 또는 1
* 2 bits : 0 0 / 0 1 / 1 0 / 1 1, 네가지 담을 수 있음. 한 비트 당 2가지 담을 수 있음
* 3 bits : 8개
* 8 bits : 256개, 1 byte

### byte : 8 bits
* go, rust : int8, 16, 32 ,...

## 문자를 이용한 표기
* ASCII table : 문자열 코드 표, 문자에 따라 바이트로 표현
    * 한계점 : 다양한 다국어 언어와 문자 코드가 들어있지 않음
    
* Unicode : 2 bytes, 그 이상을 이용해 다국어 표현
    * 영어, 한국어 등을 포함해 이모지도 표현
    
## 1 바이트 처리
* B : byte
* KB : 1000 byte
* MB : 1000 KByte
* GB : 1000 MByte
* TB : 1000 GByte

### Bbyte처리
* Byte : 남겨둠
* kibibyte KB : 1024 Byte
* mebibyte MB : 1024 KByte
* gibibyte GB : 1024 MByte
* tebibyte TB : 1024 Gbyte
-> google converter (mb byte convert)
  
## Text encoding
우리가 현존하는 형태의 바이너리타입을 잘 읽을 것인가?
### UTF-8 
Unicode transformation for mat(8 bit)

by Rob and Ken

* 기존의 ASCII, Unicode 등을 모두 표현할 수 있음
* 가변 길이 유니코드 인코딩 : 필요에 의해 코드가 길어질 수 있음
* 표현방법 : 바이트가 더 필요한 경우 이진법 앞부분에 1을 추가하여 표현 
* ASCII : 1byte로 표현 가능