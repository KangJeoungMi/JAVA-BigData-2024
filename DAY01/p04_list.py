# file :  p04_list.py
# desc : 리스트

# 파이썬에는 배열이 없다. 따라서 리스트로 대신한다
even = [2,4,6,8,10]
odd = [1,3,5,7,9]

print(even)
print(even[4]) # 길이가 n일때 마지막 인덱스는 n-1

even[4] = 20
print(even) # 리스트는 인덱스의 값을 변경가능

datas = [123,45.6,True,'Hello',odd, None] # 형지정이 없기때문에 어떤자료형이든 다 리스트에 할당이 가능하다
print(datas)

# 인덱싱, 슬라이싱
print(odd[2])
print(even[0])

cpWords = ['Life', 'is', 'short']
print(cpWords[0] + cpWords[2])

print(even[1:4]) # [4, 6, 8]

# 2차원 리스트
# 3행 4열
# [[1,2,3,4],
#  [5,6,7,8],
#  [9,10,11,12]]

d2Data =  [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]

print(d2Data)
# 출력결과 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i in d2Data:
    print(i)
# 출력결과 [1, 2, 3, 4]
#          [5, 6, 7, 8]
#          [9, 10, 11, 12]

dm1col1 = [1, 2, 3, 4]
dm1col2 = [5, 6, 7, 8]
dm1col3 =  [9, 10, 11, 12]
print([dm1col1,dm1col2,dm1col3])
# 출력결과 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 리스트 연산은 문자열 연산과 동일
print(even + odd)
# 출력결과 [2, 4, 6, 8, 20, 1, 3, 5, 7, 9]
print(odd * 2)
# 출력결과 [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]

# 값 변경
even[3] = 10
print(even)
# 출력결과 [2, 4, 6, 10, 20]

del even[2] # 삭제
print(even)
# 출력결과 [2, 4, 10, 20]

# 리스트 함수
# append 리스트 제일 뒤에 추가
even.append(30)
print(even)
# 출력결과 [2, 4, 10, 20, 30]

# insert 원하는 위치 값 추가
even.insert(2, 6) # 인덱스 2에다가 6을 추가
print(even)
# 출력결과 [2, 4, 6, 10, 20, 30]

# 정렬