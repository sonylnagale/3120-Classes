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


