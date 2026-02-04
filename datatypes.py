age = 87  #integer
length = 45.6 #float
greetings = "Hello there" #string
hasFeathers = True #boolean

#Multiple values stored in one variable
fruits = {"Banana","Watermelon","Apple"}  #list - ordered and changeable
courses = ["MIT","Datascience","Cybersecurity"] #array - similar datatypes
cars = ("Mercedes","Ford","Nissan","Toyota") #Tuple - ordered and unchangeable
countries = {"Zambia","Canada","India"}  #unordered and unchangeable
student ={
    "firstname" : "Esther",
    "course" : "MIT",
    "age" : 190,
    "nationality" : "Kenyan",
    "gender" : "female",
} #dictionary-key value pair


print(age)
print("The length is",length)
print(fruits)
print(countries)
print(student)
print(cars)

#type casting-converting one database to another
print(float(age))
print(int(length))