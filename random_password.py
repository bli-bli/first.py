# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# http://naver.com
# 규칙 1: http://naver.com
# 규칙 2: 처음 만나는 점(.)이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!" (!)로 구성

# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"

etc_domain = url.replace("http://", "") # naver.com
etc_domain = etc_domain[0:etc_domain.index(".")] # naver

password = etc_domain[0:3] # nav
new_password = password + str(len(etc_domain)) + str(url.count('e')) + '!'

print(f"{url} 의 비밀번호는 {new_password} 입니다.")