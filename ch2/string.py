# 파이썬 자료형
# 1. 문자열
# "", '', """ """, ''' '''  <== 문자열 담기 (3개짜리는 여러줄 넣을 때)

# + : 결합
print("Python " + "is fun")

# * : 복제(곱하기)
print("Python" * 3)

print("*" * 50)
print("내 프로그램")
print("*" * 50)

# 인덱싱 : 문자열은 인덱스 값을 가지고 있음(0부터 시작)
str1 = "Life is too short"
print(str1[3])

# 슬라이싱 [시작위치 : 끝위치] => 끝 위치 포함하지 않음
print("str1[2:6]", str1[2:6])
print("str1[:6]", str1[:6]) # 시작위치 지정하지 않은 경우 0부터 시작
print("str1[:]", str1[:]) # 위치 지정하지 않은 경우 0 ~ 끝까지
print("str1[:-4]", str1[:-4]) # - 값은 오른쪽 끝에서부터 위치를 잡는경우 -1부터 시작
# (-는 - 지정범위 빼고 전부 출력)

# len() : 길이 함수
print("str1 길이", len(str1))

str2 = "20230615Sunny"
# 년도, 날씨를 구별해서 변수에 담기
date = str2[:8]
weather = str2[8:]
print(date, weather)


# date 변수에 담긴 값을 년-월-일
year = str2[:4]
month = str2[4:6]
day = str2[6:8]
print(year, month, day, sep="-")

# 주민등록번호 001205-32324567
# 남자(1,3) / 여자(2,4) 출력
str3 = "001205-32324567"
no = str3[7]
if no == "1" or no == "3":
    print("남")
elif no == "2" or no =="4":
    print("여")

print()
str1 = "대한민국"
for s in str1:
    print(s+"$", end="")

print()
# 입력받은 숫자만큼 하트 출력
# 54321
# ♥♥♥♥♥
# ♥♥♥♥
# ♥♥♥
# ♥♥
# ♥
# num = input("숫자입력 : ")
# for i in range(len(num)):
#     for j in range(int(num[i])):
#         print("♥", end="")
#     print()

# 문자열 관련 함수
# count
print("\n문자열 관련 함수")
str1 = "hobby"
print("원본 문자열에 포함된 특정문자 개수 : ",str1.count("b"))

str1 = "python is best choice"

# find()
print("찾는 문자의 시작 위치 반환", str1.find("b"))
print("찾는 문자의 시작 위치 반환", str1.find("k"))
print("찾는 문자의 시작 위치 반환", str1.find("i",10))

# index() : 못찾는 경우 ValueError 발생
print("찾는 문자의 시작위치 반환 ", str1.index("b"))

# startswith() /endswith() : 특정 문자열로 시작하는지 / 끝나는지
print(str1.startswith("p"))
print(str1.endswith("p"))

# join
str2 = ","
print("문자열 삽입 :", str2.join("abcde"))

# upper() / lower()
print("abcdef".upper()) # ABCDEF
print("ABCDEF".lower()) # abcdef

# swapcase() : 대문자 -> 소문자, 소문자-> 대문자
str1 = "Python is Easy"
print(str1.swapcase())
print("abc" == "ABC")

# 공백 제거 : 왼쪽, 오른쪽, 양쪽
str1 = "     hi"
print(str1.lstrip())
str2 = "hi       "
print(str2.rstrip())
str3 = "  hi  "
print(str3.strip())

# replace()
str1 = "Life is too short"
print("특정 문자열 변경", str1.replace("Life","Your leg"))

# split() => [](리스트)로 반환
print(str1.split()) #['Life', 'is', 'too', 'short']

a = "abcd"
print(a.split()) # ['abcd']

a = "a:b:c:d"
print(a.split(":")) # ['a', 'b', 'c', 'd']

a = "하나\n둘\n셋"
print(a.splitlines()) # ['하나', '둘', '셋']
print(a.split()) # ['하나', '둘', '셋']

# 문자열 구성 파악 - isdigit(), isalpha(), isalnum(), islower(), isupper()
print("12345".isdigit()) # 숫자로만 구성되어 있느냐?
print("12345".isalpha()) # 알파벳으로 구성되어 있느냐?
print("12345".isalnum()) # 알파벳 or 숫자로 구성되어 있느냐?

# 사이트별 비밀번호를 만들어 주는 프로그램작성
# https://www.naver.com

# 규칙 1 : https://www. 제외
# 규칙 2 : 처음 나오는 . 이후 부분은 제외
# 규칙 3 : 남은 글자중 처음 세자리 + 글자개수 + 글자 내 e의 개수 + ! 로 구성
# 완성된 비밀번호 : nav51!
str1 = "https://www.naver.com"
str2 = str1.replace("https://www.","")
num1 = str2.find(".")
str3 = str2[:num1]
str4 = (str3[:3] + str(len(str3)) + str(str3.count("e")) + "!")
print(str4) # nav51!

