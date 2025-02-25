class Animal:
    def __init__(self, name, species="Unknown", age=0, sound="..."):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__sound = sound
        print(f"Hello, I am {self.__name}, a {self.__species}.")

    def talk(self):
        print(f"{self.__name} says: {self.__sound}")

    def get_species(self):
        return self.__species

    def set_species(self, species):
        self.__species = species

    def set_sound(self, sound):
        self.__sound = sound

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

    def describe(self):
        print(f"{self.__name} is a {self.__age}-year-old {self.__species} that says '{self.__sound}'.")


