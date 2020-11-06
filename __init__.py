# __init__ 생성자 : 객체가 생성될 때 사용
# 멤버변수 : 클래스 내에서 정의된 변수
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 멤버변수를 추가로 할당이 가능하다
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
