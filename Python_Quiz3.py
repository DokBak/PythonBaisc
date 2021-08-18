#퀴즈3

# URL을 기준으로 비밀번호을 생성한다.
# http://naver.com

# 규칙1 http://는 생략
# 규칙2 처음만나는 .이후부분은 제외 -> naver
# 규칙3 남은 글자중 처음 세 자리 + 글자갯수 + 글자 내 'e'의 갯수 + '!'로 구성

#URL="http://naver.com"
#URL = "http://daum.net"
#URL = "http://google.com"
URL = "http://youtube.com"

#규칙1 적용
URL=URL[7:]
#규칙2 적용
URL=URL[:URL.find(".")]
#규칙3 적용
a = URL[:3]
b = len(URL)
c = URL.count("e")

print(str(a)+str(b)+str(c)+"!")
