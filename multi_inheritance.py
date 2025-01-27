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
# 드랍쉽 : 공중 유닛, 수송기, 마린/ 파이버뱃/ 탱크 등을 수송 / 공격불가
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# 공중 공격 유닛 클래스
# 다중상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
