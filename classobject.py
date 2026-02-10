#CLASS IS A BLUEPRINT OF AN OBJECT
#OBJECT IS AN INSTANCE OF A CLASS

class Employee:
    # attributes/variables
    name = "James"
    age = 45
    gender = "male"
    salary = 70000.00

    # behaviour/function
    def work(self):
        print("Employee works")


employee1 = Employee()  # creating an object
print(employee1.name)
employee2 = Employee()
employee3 = Employee()




