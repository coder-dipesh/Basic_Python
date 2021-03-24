'''
Que.7: Given a positive real number. print its fractional part.
'''

number=float(input('Enter number to get its fractional part: '))

integePart=int(number)

fractional_part= number-integePart

print(integePart)
# print(f'{fractional_part} is the fractional part of given number.'