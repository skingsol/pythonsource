# 주석
"""
여러줄 주석 처리는 " 3개로 사용 
"""
'''
여러줄 주석 처리에 ' 3 개도 가능
'''

# 화면출력 = print() / 변수타입 확인 - type() 
print("Hello Python!!!")
print("100")
print(25.3)
print(type(100)) # <class 'int'>
print(type("100")) # <class 'String'>
print(type(100.15)) # <class 'float'>
print(type(True)) # <class 'boolean'>

# sep : 세퍼레이터 옵션 문자열 사이 구분자(기본값 스페이스바 한번)
print('t','e','s','t') # t e s t
print('t','e','s','t',sep='') # test
print('t','e','s','t',sep='-') # t-e-s-t

# end : 기본값은 엔터, ' ' 로 하면 한칸띄고 같은줄에 다음구문 연결 출력
print("Wellcome To",end=' ')
print("the black prade")

# format : %s(문자열,정수,실수), %d(정수), %f(실수), %c(문자열 하나)
# 자바에서 print( , )에서 , 대신 파이썬에서는 % 쓴다
print("%d" % 100) # 정수출력
print("%5d" % 100) # 5자리 맞춰서 오른쪽정렬 출력
print("%05d" % 100) # 5자리 맞춰서 오른쪽정렬 출력(공백은 0으로 채워주세요)
print()
print("%s" % "hi") # 문자열출력
print("%5s" % "hi") # 5자리 맞춰서 오른쪽정렬 출력
print()
print("%-8.2f" % 123.21) # - 붙이면 왼쪽정렬, 8자리로, 소수점뒤는2자리로
print("%8.2f" % 123.21)
print("%8.2f" % 123.213456)

# 변수 선언(타입 선언 안함 - 값에 따라 타입 결정)
number = 3
print("I eat %d" % number) # %d자리잡아주고 호출 I eat 3 으로 출력됨
print("I eat", number, "apples") # I eat 3 apples

print("%d : %s" % (1, "홍길동")) # 1 : 홍길동  (여러개가 대입되야되는 경우는 괄호사용)

print("I eat %s apple" % 2) #I eat 2 apple
print("I eat %s apple" % 3.156) #I eat 3.156 apple
print("I eat %s apple" % "two") #I eat two apple

# 98% 출력하기
print("Error is %d%%" % 98) # Error is 98% (퍼센트 사용하고 싶을때는 한번더 사용)

# format() 함수
print("forrmat 함수 : {}")
print("{} and : {}".format("You","Me")) # You and : Me
print("I eat {} apples".format(3)) # I eat 3 apples
print("{0} and {1} and {0}".format("You","Me")) # You and Me and You
print("{var1} and {var2}".format(var1="You",var2="Me")) # You and Me
print("{0} and {var2}".format("You",var2="Me")) # You and Me

# 이스케이프 문자 : \n, \t
print("\n줄바꿈\n연습") # \n 줄바꿈
print("띄어쓰기\t연습") # \t tab키 띄어쓰기
print("\\") # \출력하려면 \\ 으로 입력
print(r"\n \t \\ 그대로 출력") # r은 그대로 출력
print("글자가 '강조'되는 효과") # 반대로도 적용가능, 문자 표현시 "",'' 허용

