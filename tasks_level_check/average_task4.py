#Task 4: Student Average Grade
#Description : Create a dictionary to store the grades of students in a class (keys:
#student names, values: grades). Write a function to calculate the average grade of the
#class.
# I was not aware of the dictionary function, so did it with lists instead. Understood what dictionaries are and why we should use them here instead of list.
# For this specific task it works since we do not shuffle the lists. 
# Program using dictionary is present in the "other" folder.

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