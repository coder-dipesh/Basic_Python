"""
Write a Python program to convert seconds to day, hour, minutes and seconds.
"""
raw_input = int(
    input('Enter the time to convert into minutes,hour and day(input in seconds):'))
minutes = raw_input/60
hour = minutes/60
days = hour/24
print(f'Output in minutes is {minutes} mins.')
print(f'Output in hour is {hour} hrs.')
print(f'Output in day is {days} day.')
