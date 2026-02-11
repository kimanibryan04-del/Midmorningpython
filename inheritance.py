#parent class/super class/base class
class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")

#child class/sub Class/derived class

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")

class Donkey(Animal):
    def move(self):
        print("Donkey is moving")

a = Animal()

c = Cat()

d = Donkey()