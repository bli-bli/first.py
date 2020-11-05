absent = [2,5] #결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue # 아래의 코드를 실행하지 않고 skip
    elif student in no_book: # 코드를 멈춤
        print("오늘 수업은 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))