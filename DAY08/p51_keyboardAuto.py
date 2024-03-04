# file: p51_keyboardAuto.py
# desc: 키보드 자동화 with pyAutoGui

'''
파이썬 모듈 설치시는 명령 프롬프트보다 vscode내 터미널에서 설치를 추천
모듈 설치
> pip install pyperclip
'''


import pyautogui as auto
import pyperclip as clip

# auto.mouseInfo()
auto.click(485,591)
auto.write("print('hello python')", interval=0.1)
auto.write("\n", interval=0.01)
auto.typewrite("print('Life is short , you need python')", interval=0.1) # write()와 동일

#  키보드 프레스
auto.press('enter')
auto.press('A')

# # 키보드 단축키로 입력
# auto.hotkey('ctrl','a') # 전체 선택
# auto.hotkey('ㅔ갸ㅜㅅ('ㅗctrl','c') # 복사
# auto.press('esc')
# auto.press('\n')

# auto.hotkey('ctrl', 'v') # 붙여넣기

# 한글은 pyautogui에서 입력할 수 있음
clip.copy('안녕하세요 파이썬입니다. ') # 클립보드에 한글 내용을 저장

auto.hotkey('ctrl', 'v') # 붙여넣기