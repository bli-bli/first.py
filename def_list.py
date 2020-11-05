# 리스트 []
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# append : 하하씨가 다음 정류장에서 다음 칸에 탐, 항상 맨 뒤에 붙여줌
subway.append("하하")

#insert : 정형돈씨를 유재석씨와 조세호씨 사이에 넣음
subway.insert(1, "정형돈")
print(subway)

# pop : 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
print(subway.count("유재석"))

# 정렬 sort, 역정렬 reverse
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

# 모두 지우기 .clear()
num_list.clear()

# 다양한 자료형 함께 사용 , 리스트 확장 .extend()
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, False]
num_list.extend(mix_list)
print(num_list)





