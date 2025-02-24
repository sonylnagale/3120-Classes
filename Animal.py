class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")

    def swim(self):
        print("blub blub")

    def breach(self):
        print("splash")

    def echolocate(self):
        prnt("ping")