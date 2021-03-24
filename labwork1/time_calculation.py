#Question No:4
#Given the integer N-the NUmber of minutes that is passed since midnight - how many
#hours and minutes are displayed in the 24 hour digital clock?
#The program should print two numbers : the numbers of hours(between 0 and 23) and the number of minutes (between 0 and 59)
#For example , if N=150 then 150 minutes  have passed since midnight -i.e now is 2:30 a . So, the program should print 2:30.



total_time = int(input("Please enter min passed after midnight : "))
hour = total_time // 60
min = total_time % 60

print('The current time is ', hour , ':' , min)
print(f"The current time is {hour}:{min} AM.")





