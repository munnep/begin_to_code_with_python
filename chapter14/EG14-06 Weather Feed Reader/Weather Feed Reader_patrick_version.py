import urllib.request
import xml.etree.ElementTree

# EG14-06 Weather Feed Reader

def get_weather_temp(latitude,longitude):
    address = 'http://forecast.weather.gov/MapClick.php' 
    query = '?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml'.\
            format(latitude,longitude)
    # print(address + query)        
    req=urllib.request.urlopen(address+query) 
    page=req.read() 
    doc=xml.etree.ElementTree.fromstring(page) 
    for d in doc.iter('temperature'): 
        if d.get('type') == 'apparent': 
            text_temp_value = d.find('value').text 
            return int(text_temp_value) 

def get_weather_temp_max(latitude,longitude):
    address = 'http://forecast.weather.gov/MapClick.php' 
    query = '?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml'.\
            format(latitude,longitude)
    # print(query)        
    req=urllib.request.urlopen(address+query) 
    page=req.read() 
    doc=xml.etree.ElementTree.fromstring(page) 
    for d in doc.iter('temperature'): 
        if d.get('type') == 'maximum': 
            text_temp_value = d.find('value').text 
            return int(text_temp_value) 
        
def get_weather_temp_min(latitude,longitude):
    address = 'http://forecast.weather.gov/MapClick.php' 
    query = '?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml'.\
            format(latitude,longitude)
    # print(query)        
    req=urllib.request.urlopen(address+query) 
    page=req.read() 
    doc=xml.etree.ElementTree.fromstring(page) 
    for d in doc.iter('temperature'): 
        if d.get('type') == 'minimum': 
            text_temp_value = d.find('value').text 
            return int(text_temp_value)         
    
if __name__ == '__main__':
    temp = get_weather_temp(latitude=47.61, longitude=-122.33)
    print('The temperature is:', temp)
    
    temp_max = get_weather_temp_max(latitude=47.61, longitude=-122.33)
    print('The maximum temperature is:', temp_max)
    
    temp_min = get_weather_temp_min(latitude=47.61, longitude=-122.33)
    print('The minimum temperature is:', temp_min)

