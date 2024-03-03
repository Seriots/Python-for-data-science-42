from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)
try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print(e)

try:
    student = Student(name="Edward", surname="agle", login="toto")
    print(student)
except TypeError as e:
    print(e)

student = Student(name=123, surname="agle")
print(student)
