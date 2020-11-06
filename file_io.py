# score.txt 파일을 열어서 write 를 하기 위한 목적으로 열고 한글은 utf-8로 열어주도록 하겠다.
# w 를 할시에는 덮어쓰기가 된다
score_file = open("score.txt", "w", encoding="utf8")
print("과학 : 0", file=score_file)
print("수학 : 90", file=score_file)

# a 를 할시에는 append 추가하기가 된다
score_file = open("score,txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# r 은 reading, 전체 불러오기
score_file = open("score_file", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# r 은 reading, 한 줄 읽고 커서는 다음 줄로 이동, 읽어올 텍스트가 몇 줄일지 알 때
score_file = open("score_file", "r", encoding="utf8")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
score_file.close()

# 읽어올 텍스트가 몇줄인지 모를 때
score_file = open("score_file", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end=" ")
score_file.close()

# list에 넣어서 처리
score_file = open("score_file", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end=" ")
score_file.close()










