#file: p16_io.py
#desc: 입출력 학습

# input() 함수 기본
# res = input('Say Hi >> ')
# print(res)

# num = input('mutiple number >> ')
# print(type(num))
# # input() 으로 받는 값은 모두 문자열이다
# num = int(num)
# print(num*2) 
# # 숫자를 입력받아서 계산등을 할때는 형변환이 필요

# num = int(input('multiple of two >>'))
# print(num*2)

# 여러값 입력
# int(40.2) # 40
# int('50') # 50
# int('40.2') # (x)
# 튜플의 괄호중 할당을 받는 쪽의 괄호()는 생략 가능
# int(10,20,30) # (x) 튜플 바로 int로 변경할 수 있는 방법이 없음
# (a1, a2, a3) = int(input('3개 값을 입력(구분자 space) > ').split(' '))
(a1, a2, a3) = map(int,input('3개 값을 입력(구분자 space) > ').split(' '))
print(a1)
print(a2)
print(a3)
sum = a1+a2+a3
print(f'합계는 {sum}')