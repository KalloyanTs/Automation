#Task 4: Student Average Grade
#Description : Create a dictionary to store the grades of students in a class (keys:
#student names, values: grades). Write a function to calculate the average grade of the
#class.

class_size = int(input("How many students are there in class:"))
list_of_names = []
grades_list =[]

for n in range(class_size):
    student_name = str(input(f"Name of student #{n+1}:"))
    student_grade = int(input("Grade score:"))
    list_of_names.append(student_name)
    grades_list.append(student_grade)

sum_score = sum(grades_list)

print(f"The average score for the class is:{sum_score/class_size} ")