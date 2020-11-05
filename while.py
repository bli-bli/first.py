# 스타벅스에서 손님이 주문한 커피가 나왔는데 총 5번을 부를 때 까지 손님이 오시지 않을 경우
# 커피를 버리를 정책을 만들었다고 가정
# while (5번의 제한)
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index ==0:
        print("커피는 폐기처분되었습니다")

# while (true)
customer = "아이언맨"
while True:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

# while
customer = "조은비"
person = "unknown"
while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("성함이 어떻게 되세요?")