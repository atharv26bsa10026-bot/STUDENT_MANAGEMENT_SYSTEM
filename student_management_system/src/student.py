

class Student:
    def __init__(self, name, registration_no, marks):
        self.name = name
        self.registration_no = registration_no
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def percentage(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        percent = self.percentage()

        if percent >= 90:
            return "A"
        elif percent >= 80:
            return "B"
        elif percent == 100:
            return "S"
        elif percent >= 70:
            return "C"
        elif percent >= 60:
            return "D"
        elif percent >= 40:
            return "E"
        else:
            return "F"

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Registration Number:", self.registration_no)
        print("Subject 1 Marks:", self.marks[0])
        print("Subject 2 Marks:", self.marks[1])
        print("Subject 3 Marks:", self.marks[2])
        print("Total:", self.total_marks())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())