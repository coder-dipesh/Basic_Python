'''
If name is less than 3 characters long name must be at least 3 characters otherwise if it's more than 50 characters name must be maximum
of 50 characters otherwise - name looks good!
'''


user_name= input('Enter your name: ')
length=len(user_name)
if length<3:
    print("Name must be at least 3 characters.")
elif length>50:
    print("Max length must be of 50 characters.")
else:
    print("The name looks good.")

