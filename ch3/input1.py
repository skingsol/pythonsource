# 파일 읽기
# r : read
# f = open("resource/test1.txt", "r", encoding="utf-8")
# print(f.read())
# f.close()

# with open("resource/test1.txt", "r", encoding="utf-8") as f:
#     print(f.read())


# readline() 줄 단위
# f = open("resource/test2.txt", "r", encoding="utf-8")
# content = f.readline()
# print(content)
# f.close()

# f = open("resource/test2.txt", "r", encoding="utf-8")
# content = f.readline()
# while content:
#     print(content, end="")
#     content = f.readline()

# f.close()


# readlines() : 파일 내용을 리스트로 반환
# f = open("resource/test2.txt", "r", encoding="utf-8")
# content = f.readlines()
# print(content)
# f.close()


# score.txt 읽어온 후 합계, 평균 출력
# score = []
# f = open("resource/score.txt", "r", encoding="utf-8")
# for c in f:
#     # print(c.strip())
#     score.append(int(c.strip()))
# f.close()

# print(score)

# print("총계 ", sum(score))
# print("평균 ", sum(score) / len(score))


# info.txt 읽어 BMI 지수를 계산한 후 화면에 출력

# 라차, 58, 187

# 라차 58 187
# 이름 : 라차
# 몸무게 : 58
# 키 : 187
# BMI : 계산값    weight / (height / 100) ** 2
# 결과 : 저체중   bmi 지수가 25 이상 : 과체중, 18.5 이상 : 정상체중, 나머지 저체중

# f = open("resource/info.txt", "r", encoding="utf-8")
# for info in f:
#     # 변수에 담기
#     name, weight, height = info.strip().split(", ")
#     # bmi 계산
#     bmi = int(weight) / (int(height) / 100) ** 2
#     # 결과
#     if 25 <= bmi:
#         result = "과체중"
#     elif 18.5 <= bmi:
#         result = "정상체중"
#     else:
#         result = "저체중"

#     print(name, weight, height)
#     print("이름 : {}".format(name))
#     print("몸무게 : {}".format(weight))
#     print("키 : {}".format(height))
#     print("BMI : {}".format(bmi))
#     print("결과 : {}".format(result))
# f.close()


# 원본 파일(origin.txt)을 읽어서 암호화 시켜서 저장(encry.txt)한 후 암호화된 파일을 읽어
# 원래대로 출력

# print(ord('a'))  # ord() : 문자 => 코드 값 반환
# print(chr(97))   # chr() : 코드 값 => 문자 반환

#
# print(chr(ord('안') + 100))  # 얬

while True:
    no = int(input("1. 암호화 | 2. 복호화 | 3. 종료 "))
    if no == 1:
        # 내용 읽기
        with open("resource/origin.txt", "r", encoding="utf-8") as f:
            content = f.read()

        # 암호화 작성 파일 작성
        with open("resource/encry.txt", "w", encoding="utf-8") as f:
            for c in content:
                f.write(chr(ord(c) + 100))
    elif no == 2:
        # encry.txt 읽어온 후 원래 내용으로 화면 출력
        with open("resource/encry.txt", "r", encoding="utf-8") as f:
            content = f.read()
            for i in range(len(content)):
                print(chr(ord(content[i]) - 100), end="")
    else:
        break

# rb, wb : read binary, write binary ==> text 파일 아닌 것들
