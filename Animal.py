class Animal:
    def __init__(self, name, species, gender):
        self.__name = name
        self.__species = species
        self.__gender = gender
        print("hello I am", self.__name)


    def talk(self):
        print(self.__name)

    def print_species(self):
        print("I am a",self.__species)

    def print_gender(self):
        print("I am a",self.__gender)

    def excrete_waste(self):
        print("I have excreted my waste")

    

