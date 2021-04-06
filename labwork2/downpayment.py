'''
Price of the house is $1M if buyer has good credit they need to put down 10 %
otherwise they need to put down 20 %
Print down payment.
'''

price= 1000000
credit= True

if credit:
    payment1=0.1*price
    print(f'Amount to be paid is {payment1}')
else:
    payment2=0.2*price
    print(f'Amount to be paid is {payment2}')

