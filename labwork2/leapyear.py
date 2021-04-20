year=int(input('Enter year to check :'))

if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            print('Leap Year')
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

