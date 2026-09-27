
from src import records
from src.student import Student


while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        registration_no = input("Enter registration number: ")
    
        marks = []
        for i in range(3):
            mark = float(input(f"Enter marks for Subject {i+1}: "))
            marks.append(mark)

        student = Student(name, registration_no, marks)
        records.add_student(student)

        print("Thank you for using the Student Management System!")

    elif choice == "2":
        records.display_students()

        print("Thank you for using the Student Management System!")

    elif choice == "3":
        registration_no = input("Enter registration number to search: ")
        records.search_student(registration_no)

        print("Thank you for using the Student Management System!")



    else:
        print("Invalid choice. Please try again.")