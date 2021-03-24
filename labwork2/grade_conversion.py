'''
WAP which acepts marks of four subjects and display total marks, percentage and grade
Hint more than 70 % >> distion, more than 60 % >> first more than 40 % >>pass less than 40 % >> fail

'''

#Asking Data
print('Enter marks obtained in each subjects. ')

math=int(input('Enter marks otained in Maths: '))
architect=int(input('Enter marks otained in Architecture: '))
programming=int(input('Enter marks otained in Programming: '))

#Display total

total_marks=(math+architect+programming)
print(f'Total marks obtained is {total_marks} out of 300.')

#Display percenage

percentage=total_marks/3
if percentage>=70:
  print("Congrats! It's distinction. ")
elif percentage>60:
  print("Congrats! It's First Division. ")
elif percentage>40:
  print("Congrats! Just Pass. ")
else:
  print('Sorry! You failed')

#Displaying Grades

if percentage>70:
  print('The Grade is A+ .')
elif percentage>60:
  print('The Grade is B.')
elif percentage>40:
  print('The Grade is C.')
else:
  print('The Grade is D.')