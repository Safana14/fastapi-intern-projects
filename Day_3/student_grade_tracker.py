students={}
def add_student(name, grade):
    students[name]=grade
def update_grade(name,grade):
    if name in students:
        students[name]=grade
    else:
        print("Student not found")
def get_average():
    if students:
        return sum(students.values()) / len(students)
    return 0
def list_students():
    for name, grade in students.items():
        print(f"{name}: {grade}")
add_student("Safana",90)
add_student("John",85)
update_grade("John",95)
list_students()
print("Average Grade:",get_average())