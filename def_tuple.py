# tuple 은 list 와 달리 변경이 불가하다 그러나 속도가 빠르다
# 그래서 변경되지 않는 목록을 사용할 때 tuple 을 사용한다

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
