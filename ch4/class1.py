# class

# 학생 3 명의 정보(이름, 학년, 반, 성별, 과목점수) 저장

student_name_1 = "kim"
student_grade_1 = 1
student_number_1 = 1
student_detail_1 = [
    {"gender": "male"},
    {"score1": 95},
    {"score2": 99}
]

student_name_2 = "Park"
student_grade_2 = 1
student_number_2 = 2
student_detail_2 = [
    {"gender": "female"},
    {"score1": 88},
    {"score2": 89}
]

student_name_3 = "Hong"
student_grade_3 = 1
student_number_3 = 3
student_detail_3 = [
    {"gender": "female"},
    {"score1": 78},
    {"score2": 79}
]

# 3명의 학생 정보 출력
# 이름 : kim, 학년 : 1, 반 : 1, 학생정보 : detail 정보 출력
print("이름 : {}, 학년 : {}, 반 : {}, 학생정보 : {}".format(student_name_1, student_grade_1, student_number_1, student_detail_1))
print("이름 : {}, 학년 : {}, 반 : {}, 학생정보 : {}".format(student_name_2, student_grade_2, student_number_2, student_detail_2))
print("이름 : {}, 학년 : {}, 반 : {}, 학생정보 : {}".format(student_name_3, student_grade_3, student_number_3, student_detail_3))

print()

student_name_list = ["Kim", "Park", "Hong"]
student_grade_list = [1, 1, 1]
student_number_list = [1, 2, 3]
student_detail_list = [
    {"gender": "male", "score1": 95, "score2": 99},
    {"gender": "female", "score1": 88, "score2": 89},
    {"gender": "female", "score1": 78, "score2": 79}
]

print()

# 두 번째 학생 정보 출력
print("이름 : {}, 학년 : {}, 반 : {}, 학생정보 : {}".format(student_name_list[1], student_grade_list[1], student_number_list[1], student_detail_list[1]))