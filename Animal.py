class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print("WOOF!")
#Addtional 5 functions
    
    def eat(self, food):
        print(f"{self.__name} eats {food}.")  
        
    def sleep(self, hours):
        print(f"{self.__name} sleeps for {hours} hours.")

    def play(self):
        print(f"{self.__name} is playing fetch!")

    def groom(self):
        print(f"{self.__name} is cleaning himself with water.")

    def make_sound(self):
        print(f"{self.__name} makes a barking sound.")
