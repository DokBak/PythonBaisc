# 상속

# 메서드(Method)에서 생성한 AttackUnit클래스로는 메딕을 만들수가 없다.
# 그렇기에 이전에 만들어둔 damage변수가 없는 Unit클래스를 수정.

# class Unit:
#     def __init__(self,name,hp,damage): # 공격력인 damage 제외
#             self.name = name
#             self.hp = hp
#             self.damage = damage # 제외
#             print("{0} 유닛이 생성되었습니다.".format(self.name)) # 제외
#             print("체력 {0}, 공격력 {1}".format(self.hp, self.damage)) # 제외

class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

class AttackUnit: # 공격 유닛
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self,location): # 전달 받은 방향으로 공격
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력{2}]".format(self.name,location,self.damage)) 
    def damaged(self,damage): #damage 만큼 유닛 피해
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage)) # 데미지 정보 출력
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp)) # 남은 체력 출력
        if self.hp <= 0: # 남ㅇㄴ 체력이 0 이하이면?
            print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리

# Unit클래스와 AttackUnit클래스의 __init__() 생성자만 놓고 비교하면 겹치는 부분이 있다.
# 이럴 경우 상속이라는 개념을 통해 공통된 부분은 적지 않고도 재사용을 할 수 있다.

# 상속 방법
# class 자식클래스(상속받을_부모클래스):

# 공격 유닛
class AttackUnit(Unit): # Unit클래스를 상속
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp) # 부모 클래스의 생성자 호출
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
    def damaged(self,damage):
        print("{0} : {1} 데이지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어벳 : 공격 유닛, 화염방사기/
firebat1 = AttackUnit("파이어벳", 50, 16) # 체력 50, 공격력 16
firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
firebat1.damaged(25) # 남은 체력 25
firebat1.damaged(25) # 남은 체력 0 