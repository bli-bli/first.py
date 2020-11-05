def profile(name, age, main_lang):
    print(name, age, main_lang)

# 키워드를 이용하면 매개변수를 순서없이 호출가능하다
profile(name="유재석", main_lang=20, age="파이썬")
profile(main_lang="자바", age=25, name="김태호")