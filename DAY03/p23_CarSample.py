#file: p23_CarSample.py
#desc: Car클래스 사용해보기

from p22_carClass import Car

myCar = Car() # 클래스를 사용, 객체를 하나 생성(instance)
YourCar = Car()
print(myCar)
print(YourCar)

myCar.carNum = '10번 차 '
myCar.company = '현대자동차'
myCar.carType = '카니발'
myCar.fuelType = '가솔린'
myCar.color = '노란색'
myCar.releaseYear = 2020
YourCar.carNum = '30번 차 '

myCar.start()
myCar.accel()
YourCar.start()
myCar.turnLeft()
myCar.turnRight()
myCar.brk()
myCar.__init__()
myCar.__str__()