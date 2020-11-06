class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

class FlyableUnit2(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

# 다중 상속일 경우 super 를 사용하면 상속한 순서에 따라 하나의 클래스만 동작하게 된다
FlyableUnit()

# 다중 상속일 경우에도 super를 사용하지 않는 경우
FlyableUnit2()
