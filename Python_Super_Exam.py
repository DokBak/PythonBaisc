# 슈퍼 클래스 설명코드

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Unit,Flyable): 
#    def __init__(self):
#        super().__init__()
# 기본적으로 여러 부모클래스를 상속받아 super()클래스를 사용하면 제일 처음에 상속받은 Unit의 __init__을 상속받아 사용하게 된다.
#
# 드랍쉽
# dropship = FlyableUnit()
#
# 출력문 : Unit 생성자

# class FlyableUnit(Flyable, Unit):
#    def __init__(self):
#        super().__init__()
# 제일 처음에 상속받은 Flyable의 __init__을 상속받아 사용하게 된다.
#
# 드랍쉽
# dropship = FlyableUnit()
#
# 출력문 : Flyable 생성자

class FlyableUnit(Flyable, Unit):
   def __init__(self):
       Unit.__init__(self)
       Flyable.__init__(self)
# 드랍쉽
dropship = FlyableUnit()
#
# 출력문 : Unit 생성자
#        Flyable 생성자