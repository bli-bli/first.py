# 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 - 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5 - 15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2 번째 손님 (소요시간 : 50분)
# 총 탑승 승객 : 2분

from random import *
customers = range(1, 51)
cnt = 0
customers = list(customers)

for customer in customers:
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        cnt += 1
        continue
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
print(f"총 탑승승객: {cnt}분")

