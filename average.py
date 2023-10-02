# Average height of students
student_heights = input().split()
for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])
    print(student_heights[height])
total_height = 0
for height in student_heights:
    total_height += height
print(f"The total height is: {total_height}")

total_students = 0
for student in student_heights:
    total_students += 1
print(f"The total number of students are: {total_students}")

average = round(total_height / total_students)
print(f"The average height is: {average}")
