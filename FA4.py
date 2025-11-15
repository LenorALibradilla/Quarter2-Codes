
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
total_marks = 0
for i in range(students):
    print(f"\nEntering marks for Student {i + 1}:")
    total_marks_student = 0
    for j in range(subjects):
        marks = float(input(f" Enter marks for Subject {j + 1}: "))
        total_marks += marks
        total_marks_student += marks
    average_of_student = total_marks_student / subjects
    print(f" Average for Student {i + 1}: {average_of_student:.2f}")
average_marks = total_marks / (students * subjects)
print(f"\nClass Average: {average_marks:.2f}")