student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key, values in student_scores.items():
    if 91 <= values <= 100:
        values = "Outstanding"
    elif 81 <= values <= 90:
        values = "Exceeds Expectations"
    elif 71 <= values <= 80:
        values = "Acceptable"
    elif values <= 70:
        values = "Fail"
    student_grades.update({key : values})

print(student_grades)