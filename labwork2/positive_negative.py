'''
Que 5:
For given integer x, print 'True' if it is positive print 'False' if it is negative and print 'Zero'
if it is 0. 

'''
x=int(input('Enter number to check positive negative or zero : '))

#Checking condition
if x>0:
  print('True')
elif x==0:
  print('Zero')
elif x<0:
  print('Negative')