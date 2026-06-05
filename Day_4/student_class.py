class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_highest(self):
        if len(self.grades) == 0:
            return None
        return max(self.grades)

    def get_lowest(self):
        if len(self.grades) == 0:
            return None
        return min(self.grades)
    print("\n Student Grades")

student = Student("Safana")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.add_grade(95)
print("Average:", student.get_average())
print("Highest:", student.get_highest())
print("Lowest:", student.get_lowest())