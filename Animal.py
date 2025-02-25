class Animal:
    def __init__(self, name, fly, swim, climb):
        self.__name = name 
        self.__fly = fly
        self.__swim = swim
        self.__climb = climb
        print(f"hello, I am {self.__name}")
       

    def talk(self):
        print("hi")

<<<<<<< HEAD

    def fly (self):
        print(self.__name, "can fly")
=======
    def fly(self):
        print(self.__fly, "can fly")
>>>>>>> 7e15d3d (updated file)

    def swim(self):
        print(self.__swim, "can swim")

    def climb(self):
<<<<<<< HEAD
        print(self.__climb, "is able to climb")
        
    def swim(self):
        print("blub blub")

    def breach(self):
        print("splash")

    def echolocate(self):
        prnt("ping")

=======
        print(self.__climb, "can climb")
>>>>>>> 7e15d3d (updated file)
