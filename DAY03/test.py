# Q1
def is_odd(number):
    
    if number%2 == 0:
        return True
    else:
        return False
    
print(is_odd(3))
print(is_odd(6))

#Q2

def avg_numbers(args):
    result = 0
    for i in args:
        result += i
    return result/len(args)
# print(avg_numbers(1,2))
# print(avg_numbers(1,2,3,4,5))

#Q3
input1 = int(input('x : '))
input2 = int(input('y : '))

total = (input1+input2)
print(total)

#Q4
print("you""need""python") # youneedpython
print("you"+"need"+"python") # youneedpython
print("you", "need", "python") # you need python
print("".join( ["you","need","python"])) # youneedpython

#Q5
f1 = open('./day03/test.txt', mode = 'w', encoding= 'UTF-8')
f1.write('Life is too short\n2') 
f1.close()

f2 = open('./day03/test.txt',mode='r',encoding='utf-8')
print(f2.read())
f2.close()

#Q6
user_input = input('text : ')
f = open('./day03/test.txt',mode='w',encoding='utf-8')
f.write(user_input)
f.write('\n')
f.close()