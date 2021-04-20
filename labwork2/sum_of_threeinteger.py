"""

WAP to sum of three integers. However,if two values are equal sum will be zero

"""

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))

if  (a==b) or (b==c) or (a==c):
    print("Sum is 0.")
else:
    total=a+b+c
    print(f"The sum is {total}")