"""
N students take K apples and distribute them among each other evenly.The remaning
(the undivisible ) part remains in thee basket
How many apples will each single students get?
How many apples will remains in the basket?
The program reads the numbers N and K.
It should print two answers for the questions above.

"""

no_of_students = int(input("Enter the number of students: "))
no_of_apple = int(input("Enter numbers of apple: "))

apple_distributed = no_of_apple // no_of_students

remaning_apple = no_of_apple % no_of_students

print(f"Apple distributed in students are  {apple_distributed} ")

print(f"The remaning apple in basket are {remaning_apple}")


# print("The apple is " + str(apple_distributed))