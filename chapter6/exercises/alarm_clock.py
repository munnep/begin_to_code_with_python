import time 

alarm_time = input('What time do you want to have an alarm? format HH24:MI ')
while True:

    current_time = time.localtime() 

    hour_string = str(current_time.tm_hour)
    minute_string = str(current_time.tm_min)
    second_string = str(current_time.tm_sec)
    time_string = hour_string+':'+minute_string+':'+second_string
    time_string_minute = hour_string+':'+minute_string
    print(time_string)
    if alarm_time == time_string_minute:
        print('ALARM!!!!!!!!!!!!!')

    time.sleep(1)
