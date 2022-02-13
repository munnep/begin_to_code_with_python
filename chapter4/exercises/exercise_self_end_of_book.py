# EG4-05 Seattle Temperature 

import snaps
import time

fahrenheit = snaps.get_weather_temp(latitude=47.61, longitude=-122.33)

fahrenheit_int = int(fahrenheit)

degrees = (fahrenheit_int-32)/1.8

degrees_string = str(degrees)



# print('The temperature in Seattle in degrees is:', degrees)



snaps.display_message('Degrees Seattle' + degrees_string)
time.sleep(5)