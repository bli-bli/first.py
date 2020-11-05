cabinet = {3:"유재석", 100:"김태호"}

# 값을 가져오는 2가지 방법
print(cabinet[3])
print(cabinet.get(3))

# 없는 값을 가져오려고 할 때 default 값을 주는 방법
print(cabinet.get(5, "사용가능"))

# 해당 하는 키값이 있는지 확인하는 방법
print(3 in cabinet) # true
print(5 in cabinet) # false

cabinet = {"A-3": "유재석", "B-3": "김태호"}
print(cabinet["A-3"])
print(cabinet.get("B-3"))

# 새로운 손님을 할당하는 방법
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모두 지우기 .clear()
cabinet.clear()
print(cabinet)



