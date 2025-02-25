class Animal:
    def __init__(self, name, fly, swim, climb):
        self.__name = name 
        self.__fly = fly
        self.__swim = swim
        self.__climb = climb
        print(f"hello, I am {self.__name}")

    def fly(self):
        print(self.__fly, "can fly")

    def swim(self):
        print(self.__swim, "can swim")

    def climb(self):
        print(self.__climb, "can climb")
