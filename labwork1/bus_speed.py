'''
You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the
10 stops on the way. How long will the bus journey take? Alternatively, you could run to university. 
You jog the first mile at 7mph; then run the next two at15mph; before jogging the last at 7mph again. 
Will this be quicker or slower than the bus?

'''

# For Bus
bus_distance = 4  # in miles
bus_speed = 25  # in miles per hour
waiting = (2*10)/60    # in minutes
# total_stop = 10  # no of stop
total_time_taken_by_bus = bus_distance/(bus_speed/60) + waiting

# For running
jog_1 = 1/7
jog_2 = 2/15
jog_3 = 1/7
total_jogging_time = (jog_1+jog_2+jog_3)/60

if total_time_taken_by_bus > total_jogging_time:
    print(f"Jogging is fastest way to reach university.")
else:
    print("Bus is best option to reach university.")
