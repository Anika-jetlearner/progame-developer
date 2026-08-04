class Animals:
    def __init__(self):
        self.colour=""
        self.species=""
        self.legs=""
        self.skintype=""
    def get_details(self):
        self.colour=input("what is the colour?")
        self.species=input("what is the species?")
        self.legs=input("how many legs?")
        self.skintype=input("what is the skintype")
    def display_details(self):
        print(self.colour)
        print(self.species)
        print(self.legs)
        print(self.skintype)

cat=Animals()
cat.get_details()
cat.display_details()

dog=Animals()
dog.get_details()
dog.display_details()
