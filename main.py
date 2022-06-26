# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



""""Task 1 - Flower
Write a Python class named Flower, that has three nonpublic attributes of type str,
int, and float, that respectively represent the name of the flower, its number of
petals, and its price. Include a constructor method that initializes each variable to an
appropriate value as well as methods for setting the value and retrieving the value of
each type"""""

class Flower:
    def __init__(self,name,petals,price):
        self.name = name
        self.petals = petals
        self.price = price

    def set_name(self,name):
        self.name = str(name)

    def set_petals(self,petals):
        self.price = int(petals)

    def set_price(self,price):
        self.price = float(price)


    def get_name(self):
        return self.name

    def get_petals(self):
        return self.petals

    def get_price(self):
        return self.price

R = Flower("Rose",10,985.544)
R.set_name("Rose")
R.set_petals(10)
R.set_price(985.544)

print(R.get_name())
print(R.get_petals())
print(R.get_price())




