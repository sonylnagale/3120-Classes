#class of Animal
class Animal:


    def __init__(self, name, action, age, toy, sleep):
        self.__name = name 
        self.__action = action
        self.__age = age 
        self.__toy = toy
        self.__sleep = sleep
        print("hello, I am", self.__name)

    def action(self):
        print(f"I'm {self.__action} in the water")
    def eat(self, food):
        print(f"I like eating {food}")
    def age(self):
        print(f"I'm {self.__age} years old")
    def toy(self):
        print(f"I enjoy playing with a {self.__toy}; it's my favorite toy")
    def sleep(self):
        print(f"Did you know us otters hold hands while we {self.__sleep} so we don't drift apart?")

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

    def __init__(self, name, eye, food, speed=5, favorite_animal=""):
        self._name = name
        self._eye_color = eye
        self._food = food
        self._speed = speed
        self._favorite_animal = favorite_animal
        print(f"Hello, I am {self._name}")

    def talk(self):
        print("Hi there! I am an animal")

    def eat(self):
        print(f"{self._name} has {self._eye_color} eyes and eats {self._food}, yum yum!")
        print(f"Speed before eating: {self._speed}")
        self._speed += 1  # Increase speed after eating
        print(f"Speed after eating: {self._speed}")

    def likes(self):
        print(f"{self._name} likes {self._favorite_animal}!")

    def eye_color(self):
        return self._eye_color

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        if speed >= 0:
            self._speed = speed
        else:
            print("Speed cannot be negative.")



    #function of habitat that the animal lives in
    def habitat(self):
        print(f"As a {self.__animal_type} I live in {self.__habitat}")

    #function of the class that the animal belongs to
    def classes(self):
        print(f"We {self.__animal_type} are {self.__classes}")

    #function of printing hi
    def talk(self):
        print("hi")