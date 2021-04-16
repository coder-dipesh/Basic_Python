# '''
#
# Given a three-digit number. Find sum of its digit.
#
# '''
#
# total=0
# three_digit=input('Enter three digit number by seprating with space: ')
#
# digit=three_digit.split()
# print(digit)
#
# for i in range(0,len(digit)):
#     digit[i]=int(digit[i])
#
#
# total= total + digit[i]
#
# print(total)
def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10) #gives last digit from user input
        n = int(n / 10) # divide the
    return sum

# Driver code
n =int(input('Enter the number to get the sum of number: '))

print(getSum(n))
