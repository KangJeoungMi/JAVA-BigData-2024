# file : p53_imgload.py
# desc : pyautogui로 화면 캡쳐하기

import pyautogui as auto

# capImg = auto.locateOnScreen('./DAY08/screen.png')
# print(capImg)
# auto.click(capImg)

auto.alert('test', title = 'pyautogui')
auto.confirm('keep going?')

text = auto.prompt('text message')
print(text)

pwd  = auto.password("password")
print(pwd)