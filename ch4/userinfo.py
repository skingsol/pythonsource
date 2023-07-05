# class UserInfo:
#     """
#     Author : Hong
#     Date : 2023.06.21
#     Description : 클래스 작성법
#     """

#     def user_info(self):
#         print("메소드 실행")


# user1 = UserInfo()
# print(user1)  # <__main__.UserInfo object at 0x000001AD3DAA71D0>
# user1.user_info()


# class UserInfo:
#     #     """
#     #     Author : Hong
#     #     Date : 2023.06.21
#     #     Description : 클래스 작성법 - 인자 있는 생성자
#     #     """

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def user_info(self):
#         return "name : {}, age : {}".format(self.name, self.age)


# # 두 명의 객체 생성
# user1 = UserInfo("홍길동", 30)
# user2 = UserInfo("김유신", 40)

# # user_info 호출
# print(user1.user_info())
# print(user2.user_info())


class UserInfo:
    #     """
    #     Author : Hong
    #     Date : 2023.06.22
    #     Description : 클래스 작성법 - 클래스 변수
    #     """

    # 클래스 변수
    user_count = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

        UserInfo.user_count += 1

    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)

    def __del__(self):
        UserInfo.user_count -= 1

    @classmethod
    def function1(cls):
        """
        클래스 메소드
        """
        print("function1 호출",cls.user_count)

    def function2(self):
        print("function2 호출")


# 객체 생성
user1 = UserInfo("홍길동", 30)
user2 = UserInfo("김유신", 20)

# 메소드 호출
print(user1.user_info())
print(user2.user_info())

# 클래스 변수 확인
print("생성된 user {} 명".format(UserInfo.user_count))
print("생성된 user {} 명".format(user1.user_count))


# user 삭제
del user1  # __del__ 메소드 자동으로 실행
print("생성된 user {} 명".format(UserInfo.user_count))


# function1(), function2() 호출
UserInfo.function1()  # TypeError: UserInfo.function1() takes 0 positional arguments but 1 was given
user2.function2()
