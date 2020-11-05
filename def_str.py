sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

# """ """ 을 이용하면 줄바꿈이 들어가있는  문장을 그대로 사용할 수 있다.
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3) # 위의 예제에서는 총 4줄이 출력된다


python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 파이썬의 첫번째 문자가 대문자 인가
print(len(python)) # 공백까지 포함한 문자열
print(python.replace("Python", "Java")) # 해당 문자열을 다른 문자로 대체한다

index = python.index("n") # n이라는 단어가 몇번째에 위치하는지를 알려준다
print(index)

index = python.index("n", index + 1) # 2번째 n 이라는 단어는 어디에 있는가
print(index)

print(python.find("n")) # n이라는 단어가 몇번째에 위치하는지를 알려준다
print(python.find("Java")) # 찾고자 하는 값이 없을 때에는 -1을 반환해준다

print(python.count("n")) #글자 내 n의 갯수




