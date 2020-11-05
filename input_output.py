# sep=" "
# end=" "

print("python", "java", sep=" vs ", end="! ")
print("무엇이 더 재밌을까요?")

# 표준 출력 vs 표준 에러 --> 로그를 찍을 때 굉장히 중요
import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

#ljust, rjust
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(4), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# 표준입력 input : str 형식
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다")
