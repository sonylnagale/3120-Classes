#class of Animal
class Animal:
    def __init__(self, name, animal_type, gender, food, habitat, classes, age=0): 
        self.__name = name
        self.__animal_type = animal_type
        self.__gender = gender
        self.__food = food
        self.__habitat = habitat
        self.__classes = classes
        self.__age = age

    #function of animal's name
    def name(self):
        print(f"hello, I am {self.__name}")

    #function of animal's gender
    def gender(self):
        print(f"hello, I am {self.__gender}")

    #function of the type of animal
    def animal(self):
        print(f"I am a {self.__animal_type}")

    #function of animal's age
    def age(self):
        print(f"I am {self.__age} years old")

    #function of the food that animal eat
    def food(self):
        print(f"I eat {self.__food}")

    #function of habitat that the animal lives in
    def habitat(self):
        print(f"As a {self.__animal_type} I live in {self.__habitat}")

    #function of the class that the animal belongs to
    def classes(self):
        print(f"We {self.__animal_type} are {self.__classes}")

    #function of printing hi
    def talk(self):
        print("hi")