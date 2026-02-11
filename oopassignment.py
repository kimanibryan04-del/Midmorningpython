class Student:
    def __init__(self, fullName, course, age, feesPaid):
        self.fullName = fullName
        self.course = course
        self.age = age
        self.feesPaid = feesPaid


student1 = Student("Alice Johnson", "Computer Science", 20, 50000)
student2 = Student("Bob Smith", "Data Science", 22, 45000)
student3 = Student("Charlie Brown", "Information Technology", 21, 55000)

print(student1.fullName,student1.course,student1.age,student1.feesPaid)
print(student2.fullName,student2.course,student2.age,student2.feesPaid)
print(student3.fullName,student3.course,student3.age,student3.feesPaid)