'''

Que.7: Given a positive real number. print its fractional part.

'''
import math


number = float(input('Enter number to get its fractional part: '))
floatt,integerr = math.modf(number)


print(f'{floatt} is the fractional part of given number.')

