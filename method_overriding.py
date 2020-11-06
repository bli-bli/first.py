# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) # 상속
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
        print("\n[공중 유닛 이동]")
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# 공중 공격 유닛 클래스
# 다중상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):
        print("\n[공중 유닛 이동]")
        self.fly(self.name, location)
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 100, 20, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 20, 3)

vulture.move("11시")
battlecruiser.move("9시")