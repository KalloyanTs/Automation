#Program that averages the grades of studens in class

class_size = int(input("How many students are there in class:"))
list_of_names = []
grades_list =[]

for n in range(class_size):
    student_name = input("Name of student #{}:".format(n+1))
    student_grade = (input("Grade score:".format(n+1)))
    list_of_names.append(student_name)
    grades_list.append(student_grade)

for n in list_of_names:
    print( "Students in class and score:" , list_of_names, grades_list)