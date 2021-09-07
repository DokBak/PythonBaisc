# 생성자(Cunstructor)
# __init__를 생성자라고 부름

# 사용자가 따로 호출하지 않아도 클래스 객체를 생성할 때 자동으로 호출되는 부분
# 객체를 생성할 때는 이 생성자의 전달값에 해당하는 갯수 만큼 값을 던져야 한다.

# 생성자 부분을 보면 self를 제외하고 name, hp, damage를 전달 받고 있으며, 아래에서 유닛을 생성할 때는 각각 3개씩 값을 던진다.

class Unit:
    def __init__(self, name, hp, damage): # 3개의 전달값
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

