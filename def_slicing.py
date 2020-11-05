jumin = "961208-1234567"

# 주민번호를 통해 성별정보 확인
print('성별' , jumin[7]) # 7번째 자리 수를 가져온다
print('연 :' , jumin[0:2]) # 0 ~ 2 직전까지 (0, 1)
print('월 :' , jumin[2:4]) # 2 ~ 4 직전까지 (2, 3)
print('일 :' , jumin[4:6]) # 4 ~ 6 직전까지 (4, 5)

print('생년월일 :', jumin[0:6]) # (0, 1, 2, 3, 4, 5)
print('뒤 7자리 :', jumin[7:]) # 7 부터 끝까지
print('뒤 7자리 (뒤에부터) : ' + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지



