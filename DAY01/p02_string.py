# file : p03 _string.py
# desc : 문자열 자료형과 연산

a = "hello World"
print (a)
b = 'hello World'
print (b)
c = "hello 'World'"
print (c)
# 탈출 문자 \n, \t 외 나머지는 파이썬에 잘 사용되지 않음 

# 문장을 여러 줄 쓰고 싶으면 \로 작성하기
d = 'hello \n'\
'I\'m Hugo'\
'Nice to meet you'
print(d)
#여러줄 문장을 쓸 때는 ''',""""
d= '''Hello ~
I'm Tom
Nice to meet you'''
print(d)

# 문자열 연산 +, *
before = 'I wanna go '
after = 'home'
print(before+after) # I wanna go home, +는 문자열을 합쳐서 하나의 문자열을 만든다
print(after * 3) # homehomehome - *는 문자열의 반복이다

# 문자열 길이 구하기
print('글자 길이 : ', len(before)) # 11
print('한글 글자 길이 : ',len('안녕하세요')) # 5

# 문자열 인덱싱, 슬라이싱
cp = 'Life is too short, You need Python'
print(cp)

# 슬라이싱
print(cp[8]) # t
#cp[8] = 'd' # 문자열은 배열이긴 하나 값을 변경할 수 없는 배열이다

#문자열 번위 슬라이싱
print(cp[12:16+1]) #short - : 뒤에 있는 숫자는 항상 +1

print(ascii('안'),ascii('녕'),ascii('하'),ascii('세'),ascii('요'),)
print(chr(97))

# 기존 문자열로 새로운 문자열을 만들때는 슬라이싱,다른 문자열로 대체필수
print(cp[0:7+1], 'long', cp[17:]) # : 뒤에 생략하면 끝까지
# 다른언어에는 없는 - 슬라이싱
print(cp[-6:])
print(cp[-11:-7]) # -로 슬라이싱 때도 :뒤에는 +1을 해줘야 한다

# 문자열 포매팅(format String)
# 파이썬에서는 %d, %s, %c 등 포맷 스트링용 연산자를 사용 빈도가 낮음
temp = 21
print('현재 온도는 %d도 입니다' %temp)
temp = 17
print('현재 온도는 %d도 입니다' %temp)

# format함수로 포맷팅(가장 일반적)
print('현재 온도는 {0}도 입니다'.format(temp))

# 날짜를 포맷으로 만들때
month = 2
day = 21
hour = 3 
mins = 18

print('오늘은 {0:02d}월 {1:02d}일 {2:02d}시 {3:02d}분 입니다'.format(month,day,hour,mins))

# 숫자 자료형
income = 6_000_000_000 #60억 : 연매출
print('올해 매출액은 {0: ,d}원'.format(income))
PI = 3.1415926536
print ('파이는 {0:.2f}'.format(PI))# 10.2f 소수점 . 까지 다 포함해서 10자리 소수점뒤로는 2자리
#print('{0:d}'.format(PI))#PI는 실수이기 때문에 (d)정수 형태로 format이 안됨

# f 포매팅 3.6(2016) 이후에 나온 최신방식
name = 'Tom'
age = 30
cont = f'나는 {name}이고, 나이는 {age}이다'
print(cont)

name = 'lily'
age = 25
print( f'나는 {name:>10}이고, 나이는 {age:03d}이다')# 03d = 세 자리 수를 만들되, 빈자리는 0으로 채움
print(  f'나는 {name:<10}이고, 나이는 {age:03.1f}이다')
# 정수는 f 포맷 사용가능 , 실수는 d포맷 사용불가

# 문자열 함수
a= 'Life is short, you need Python'
print(a.count('Life')) # 1
print(a.count('o')) # 3
print(a.find('sh')) # 8
print(a.index('t')) # 첫번째 t의 위치 12
print(a.count('k')) # index()는 count()로 갯수가 0이 아닐때만 호출
print(','.join('abcde')) # a,b,c,d,e

print(a.upper()) # 대문자로 변환
print(a.lower()) # 소문자로 변환
print(a.capitalize()) # 문장이 시작되는 첫번째 단어의 첫글자만 대문자로 변환

origin = '          Hi          '
print(f'++{origin}++')
print(f'++{origin.lstrip()}++') # 왼쪽 공백 없애기
print(f'++{origin.rstrip()}++') # 오른쪽 공백 없애기
print(f'++{origin.strip()}++') # 양쪽공백 없애기
# 단 문자 사이 공백은 없앨 수 없음

print(cp.replace('too', '').replace(' short', 'long')) 
# Life is short, you need Python -> Life is long, You need Python

# 문자열 자르기 -> 리스트(파이썬에는 배열이 없음)
cp_Words = cp.split(' ')
print(cp_Words) # ['Life', 'is', 'too', 'short,', 'You', 'need', 'Python']


