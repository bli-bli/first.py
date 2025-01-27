# 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중 : 각 개인의 키에 적당한 체중

# 성별에 따른 공식
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
    # * 함수명 : std_weight
    # * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "여":
        height = height / 100
        weight = str(height * height * 21)[:5]
        print("키 {0}cm 여성의 표준체중은 {1}kg 입니다.".format(int(height*100), weight))
    elif gender == "남":
        # weight = str(height * height * 22)[:5]
        height = height / 100
        weight = round((height * height * 22), 5)
        print("키 {0}cm 남성의 표준체중은 {1}kg 입니다.".format(int(height*100), weight))

std_weight(175, "여")
std_weight(190, "남")