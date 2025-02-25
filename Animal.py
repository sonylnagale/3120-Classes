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
