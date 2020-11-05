# 가변인자
# 매개변수의 수 마음대로 설정가능하다
# *language
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "c")
profile("김태호", 21, "swift")
