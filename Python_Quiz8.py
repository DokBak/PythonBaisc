# 퀴즈 8

# (출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년 
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self,location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        print("새로운 매물 등록")
    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


H1 = House("강남","아파트","매매","10억","2010년")
H2 = House("마포","오피스텔","전세","5억","2007년")
H3 = House("송파","빌라","월세","500/50","2000년")
#H1.show_detail()
#H2.show_detail()
#H3.show_detail()
Houses = []
Houses.append(H1)
Houses.append(H2)
Houses.append(H3)


print("총 {0}대의 매물이 있습니다.".format(len(Houses)))
for OneHouse in Houses:
    OneHouse.show_detail()
# 메서드 자체에 출력문이 있는데 이것을 다시 출력문으로 감쌀필요는 없다.
