#file: p22_carClass.py
#desc: 객체지향 클래스

class Car: 
    __carNum = '' # __변수를 지정하면 private
    carNum = ''
    company = ''
    releaseYear = 1960
    color = '흰색'
    carType = ''
    fuelType = '가솔린'
    
    def __init__(self) -> None:    
        # 생성자 -> None: 리턴할게 없음
        print('Car 객체를 생성합니다.')
        
    def __str__(self) -> str:    
        # str 객제변수를 print()할때 출력 커스터마이징 함수
        return f'내 차는 {self.company},{self.carNum} dlqslek'
            
    def getCarColor(slef):
        print(f'{slef.carNum}은 {slef.color}입니다')
        
    def start(slef):
        print(f'{slef.carNum}TurnOn')
        
    def accel(slef):
        print(f'{slef.carNum}엑셀 밟기')
    
    def brk(slef):
        print(f'{slef.carNum}멈추기')
    
    def turnLeft(slef):
        print(f'{slef.carNum}좌회전')
        
    def turnRight(slef):
        print(f'{slef.carNum}우회전')