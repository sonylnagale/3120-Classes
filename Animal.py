class Animal:
    def __init__(self, type, talk, age, gender, diet, habitat): 
        self.__type = type
        self.__gender = gender
        self.__talk = talk
        self.__age = age
        self.__diet = diet
        self.__habitat = habitat


    def get_type (self):
        print(f"This animal is a: {self.__type}")

    def make_sound (self):
        print(F"This animal makes the sound: {self.__talk}")

    def get_gender (self):
        print(f"This animal is a: {self.__gender}")
    
    def get_age (self):
        print(f"This animal is {self.__age} years old")

    def get_diet (self):
        print(f"this animal is a: {self.__diet}")

    def get_habitat(self):
        print(f"This animal lives in a: {self.__habitat}")
       