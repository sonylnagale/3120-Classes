class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)
       

    def talk(self):
        print("hi")


    def fly (self):
        print(self.__name, "can fly")

    def swim(self):
        print(self.__swim, "can swim")

    def climb(self):
        print(self.__climb, "is able to climb")
        
    def swim(self):
        print("blub blub")

    def breach(self):
        print("splash")

    def echolocate(self):
        prnt("ping")

