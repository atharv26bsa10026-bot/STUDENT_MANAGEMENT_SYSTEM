
students = []

def add_student(student):
    students.append(student)
    print("Student added successfully!")

def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students:
            student.display()

def search_student(registration_no):
    for student in students:
        if student.registration_no == registration_no:
            student.display()
            return

    print("Student not found.")