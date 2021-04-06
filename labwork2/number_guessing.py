'''
Game finding a secret number within 3 attempts using while loop
'''


secret_number=3
limit=3

while limit:
    user_num=int(input("Enter your guess number: "))
    if user_num==secret_number:
        print('You won! Guessed correct number.')
        break
    else:
        print('Sorry! wrong guess .')

else:
    print('Your max guess has ended.')