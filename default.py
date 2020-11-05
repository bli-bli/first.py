# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))
#
# profile("조은비", 25 , "자바")
# profile("유재석", 45, "파이썬")

# default : 만약 같은 학교, 같은 학년, 같은 반, 같은 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("조은비")
profile("유재석")

