class Parrot:

    # class attribute
    speices = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate the Parrot class
bac = Parrot("bac", 10)
isa = Parrot("isa", 15)

# access the class attributes
print("bac is a {}".format(bac.speices))
print("isa is also a {}".format(isa.speices))

# access the instance attributes
print("{} is {} years old".format( bac.name, bac.age))
print("{} is {} years old".format( isa.name, isa.age))