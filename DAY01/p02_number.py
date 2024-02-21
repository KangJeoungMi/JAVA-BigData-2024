# file :  p02_number.py
# desc : 숫자형 자료타입

# 일반 숫자형
age = 40 # int형 담는 변수
taxRate = 8.8 # float 형을 담는 변수

hightFloats = 4.24E10 # 지수승(float)

print('나이는',age) # 문자열이 '',"" 둘다 사용가능
print('세율은',taxRate) 
print('지수값',hightFloats)

# 특수 숫자형
binVal = 0b11111111 # 255 - 컴퓨터언어
octVal = 0o11 # 9 (1~7 10(8)) - 컴퓨터언어
hexVal = 0xFF # 255 (0~9 ABCDEF) - 컴퓨터언어

print('2진수',binVal,'8진수',octVal,'16진수',hexVal)

# 타입을 적을 필요가 없음

# 사칙연산
a,b,c = 3, 4, 9
print('a + b = ',a + b) # 더하기
print('a - b = ',a - b) # 빼기
print('a * b = ',a * b) # 곱하기
print('a / b = ',a / b) # 나누기

# 단, 나누기는 3가지로 분류
print(b / c) # 0.8 - 정확하게 실수로 나누기
print (c // b) # 2 - 정수로만 나눈 몫
print (c % b) # 1 - 정수로 나눈 나머지

print(2 ** 10) # 1024

#연산자 우선순위는 ()괄호만 잘 쓰면 된다
print((a + b) * c)
