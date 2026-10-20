class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self,course,grade):
        if grade <0 or grade >20:
            print("Invalid grade. Grade must be between 0 and 20.")
        else:
            self.grades[course] = grade
            print(f"Grade {grade} added for course {course}.")

    def average(self):
        if len(self.grades) == 0:
            return 0
        else:
            total = sum(self.grades.values())
            return total / len(self.grades)

    def best_course(self):
        if len(self.grades) == 0:
            return None
        else:
            best_course = max(self.grades, key=self.grades.get)
            return best_course
    def failed_courses(self):
        failed=[]
        for course, grade in self.grades.items():
            if grade < 10:
                failed.append(course)
        return failed
    def status(self):
        avg=self.average()
        if avg>=17:
            return "Excellent"
        elif avg>=14 and avg<17:
            return "Good"
        elif avg>=12 and avg<14:
            return "Normal"
        else:
            return "Probation"
    def report(self):
        print(f"Student Name: {self.name}, Student ID: {self.student_id}")
        print("Grades:")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
        print(f"Average Grade: {self.average()}")
        print(f"Best Course: {self.best_course()}")
        print(f"Failed Courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to the classroom.")

    def Top_student(self):
        if len(self.students) == 0:
            return None
        else:
            top_student = max(self.students, key=lambda student: student.average())
            return top_student
        
    def class_average(self):
        if len(self.students) == 0:
            return 0
        else:
            total = sum(student.average() for student in self.students)
            return total / len(self.students)

s1 = student("Zohreh Bakhshi", "S001")
s1.add_grade("Math", 18)
s1.add_grade("Science", 15)
s1.add_grade("History", 12)
s1.add_grade("Art", 8)

s2 = student("Haniyeh Danesh ", "S002")
s2.add_grade("Math", 16)
s2.add_grade("Science", 14)
s2.add_grade("History", 10)
s2.add_grade("Art", 12)

s1.report()
print("--------------------------------------------------")
s2.report()

s1.add_grade("Math", 25)
classroom = Classroom()
classroom.add_student(s1)
classroom.add_student(s2)

print(f"Top Student: {classroom.Top_student().name}")
print(f"Class Average: {classroom.class_average()}")