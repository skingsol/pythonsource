# 주차장 프로그램

# 메뉴 제공
# [1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : 

parking_lot = []

top, car_name = 0, "A"

# ord(코드값)을 chr(문자)로 돌려주는 함수
# print(ord("A"))  # 65
# print(chr(65))   # A

while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("{} 자동차 들어감. 주차장 상태 ==> {}".format(car_name, parking_lot))

                top += 1
                car_name = chr(ord(car_name) + 1)

        elif no == 2:
            if top < 0:
                print("주차장 비었음")
            else:
                parking_lot.pop()
                print("{} 자동차 빼기. 주차장 상태 ==> {}".format(car_name, parking_lot))

                top -= 1
                car_name = chr(ord(car_name)-1)
        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요")




