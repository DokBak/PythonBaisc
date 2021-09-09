# 다중상속

# 스타크래프트에는 레이스와 같은 공중 유닛도 많은데, 공중 유닛 중에서도 공격이 가능한 레이스가 있는 반면, 공격이 불가능한 드랍쉽이 있다.
# 문법 :class 자식클래스(부모클래스1, 부모클래스2, ...):

# 유닛 클래스
class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
# 공격 유닛 클래스
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

# 공중 유닛 클래스
class Flyable:
    def __init__(self, flying_speed): # 공중 이동 속도
        self.flying_speed = flying_speed
    def fly(self, name, location): # 유닛 이름, 이동 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 레이스의 경우 공격유닛, 공중유닛 이 전부다 만족한다.

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed): # 이름, 체력, 공격력, 공중 이동 속도
        AttackUnit.__init__(self,name,hp,damage) # 이름, 체력, 공격력
        Flyable.__init__(self,flying_speed) # 공중 이동 속도

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리",200,6,5) # 이름, 체력, 공격력, 공중 이동 속도
valkyrie.fly(valkyrie.name,"3시") # 3시 방향으로 발키리를 이동

