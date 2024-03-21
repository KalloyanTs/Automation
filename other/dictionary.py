name_grade = {}
class_size = int(input("How many students are there in class:"))

for n in range(class_size):
    student_name = str(input("Name of student: "))
    student_grade = int(input("Grade score: "))
    name_grade[student_name] = student_grade

sum_score = sum(name_grade.values())

print(f"The average score for the class is:{sum_score/class_size} ")
