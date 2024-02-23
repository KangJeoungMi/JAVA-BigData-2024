#file: p17_fileio.py
#desc: 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(),close() / 파이썬에서만 안닫아도 크게 지장이 없다
# 2. 통신 open(),close()
# 3. DB open(or connect), close()

# 언어체계 추가 ASCII(한글 cp949), 유니코드(UTF-8)
# 상대경로 절대경로
f = open('./day03/smaple.txt', mode = 'w', encoding= 'UTF-8')
# 파일쓰기 진행
f.write('hello, Python.\n') # 한줄 내리기 \n
f.write('안녕 파이썬\n')

f.close() # 파이썬에서만 옵션. 다른언어에선 무조건 close()