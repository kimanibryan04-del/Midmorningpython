class Dog:
    def __init__(self,name,breed,hasFur):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur

    def bark(self):
        print("woof!! woof!!")

    def locomotive(self):
        print("dog walks")

dog1 = Dog("jj","BullDog",True)
print(dog1.name,dog1.breed,dog1.hasFur)
dog2 = Dog("tony", "german shepherd",True)
print(dog2.name,dog2.breed,dog2.hasFur)
dog3 = Dog("ann","chihuahua",True)
print(dog3.name,dog3.breed,dog3.hasFur)