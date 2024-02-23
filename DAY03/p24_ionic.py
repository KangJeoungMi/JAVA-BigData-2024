#file: p24_ionic.py
#desc: Car클래스 상속

from p22_carClass import Car

class Ionic(Car) : # 상속 Car클래스를 상속받아서 ionic
    __fuelRate = 0.0 # 연비
    
    def setFuelRate(self,rate):
        self.__fuelRate = rate
    def getFuelRate(self) -> float:
        return self.__fuelRate
    
myCar = Ionic('10번 차량')
myCar.company = '기아자동차'
myCar.setFuelRate(2.35)
print(myCar)
print(f'내 차의 연비는 {myCar.getCarColor()}km/1 입니다')