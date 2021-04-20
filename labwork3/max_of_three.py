"""WA Function to find max of 3 number"""

def max_number(num1,num2,num3):

    if (num1>num2) and (num1>num3):
        print(f"{num1} is max number.")
    elif (num2>num1) and (num2>num3):
        print(f"{num2} is max number.")
    else:
        print(f"{num3} is max number.")

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))

output= max_number(num1,num2,num3)
print(output)
