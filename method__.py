# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}")

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속
        self.damage = damage

    def attack(self, location):
        print(f"\n{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"\n{self.name}: {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} :남은 hp{self.hp}")
        if self.hp <= 0:
            print(f"\n--------- {self.name} : 파괴되었습니다 ")
# 메딕 : 의무병


# 파이버뱃 : 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)