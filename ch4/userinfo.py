class UserInfo:
    """
    Author : Hong
    Date : 2023.06.21
    Description : 클래스 작성법
    """

    def user_info(self):
        print("메소드 실행")

user1 = UserInfo()
print(user1) # <__main__.UserInfo object at 0x000001DC41B87190>
user1.user_info()

class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

        def downSpeed(self, value):
            self.speed -= value

# Red, Blue, Yellow 자동차 객체 생성
car1 = Car()
car1.color = "Red"

car2 = Car()
car2.color = "Blue"

car3 = Car()
car3.color = "Yellow"

# 각각의 자동차마다 속도를 up, down 시키기
car1.upSpeed(100)
print("1번 자동차의 색상은{}이고, 속도는{}Km 입니다".format(car1.color, car1.speed))

car2.upSpeed(60)
car2.downSpeed(20)
print("2번 자동차의 색상은{}이고, 속도는{}Km 입니다".format(car2.color, car2.speed))

car3.upSpeed(150)
scr3.downSpeed(50)
print("3번 자동차의 색상은{}이고, 속도는{}Km 입니다".format(car3.color, car3.speed))
