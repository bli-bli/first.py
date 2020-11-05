# 파이썬의 경우 함수 안에서는 그 안에서만 사용하는 지역변수를 설정해주는 것이 좋다.
# 하지만 전역 변수를 사용할 경우에는 global gun이라는 것을 넣어 사용할 수 있다.
gun = 10

def checkpoint(soldiers): # 경계근무
    global gun
    gun = gun - soldiers
    print(f"[현재] 남은 총의 개수 : {gun}")
checkpoint(2)

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f"[현재] 남은 총의 개수 : {gun}")
    return gun

gun = checkpoint_ret(gun, 2)
print(gun)