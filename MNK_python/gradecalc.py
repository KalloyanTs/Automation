grade_score = int(input(""))

if grade_score > 100 or grade_score < 0:
    print("Incorrect score")
elif grade_score >= 90:
    print("A")
elif grade_score >= 80:
    print("B")
elif grade_score >= 70:
    print("C")
elif grade_score > 60:
    print("D")
else:
    print("F")
