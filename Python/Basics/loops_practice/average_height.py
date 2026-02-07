student_heights = input("Enter the Heights with Space.\n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height+= height

total_students = len(student_heights)

avg_height = round(total_height / total_students)

print(f"total height = {total_height}")
print(f"number of students = {total_students}")
print(f"average height = {avg_height:.2f}")