'''
Que.4: Given three integer print the smallest one (Three integer must be inputed by user)

'''

input1=int(input('Enter first number to check: '))
input2=int(input('Enter second number to check: '))
input3=int(input('Enter Third number to check: '))

#Main condition to check
if input1<input2 and input1<input3:
  print(f'{input1} frist number entered is smallest.')
elif input2<input1 and input2<input3:
  print(f'{input2} second number entered is smallest.')
else:
  print(f'{input3} third number entered is smallest.')