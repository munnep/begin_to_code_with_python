import time 

current_time = time.localtime() 

hour = current_time.tm_hour 
minute = current_time.tm_min
day_of_week = current_time.tm_wday


if (hour>7) or (hour==7 and minute>29):
    if day_of_week < 5:
        print('IT IS TIME TO GET UP')
    else:
        print('Go back to bed it\'s weekend')    
else:
    print('Go back to bed. To early')    
