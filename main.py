
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

# 정수형 과 boolean 자료형은 str 로 감싸주어야 한다
# 다만 , 로 문장을 이어줄 때는 str 로 감싸줄 필요가 없다. 그러나 , 가 들어가게 되면 무조건 , 가 하나씩 포함이된다.
print('우리집' + animal +'의 이름은' + name + '에요')
print(name + '는'+ str(age) +'살이며,'+ hobby +'을 아주 좋아해요')
# print(name+ '는 어른일까요?'+ str(is_adult))
print(name,'는 어른일까요?',is_adult)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
