# Chapter 14: Python programs as network clients

Send a package wover the network with python

Terminal 1
```
# socket module to import
import socket

# listen on something
listen_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# addresss to listen on
listen_address = ('localhost', 10001)

# bind the socket to listen on the address
listen_socket.bind(listen_address)

# make sure it is listening now
result = listen_socket.recvfrom(4096)
```

Terminal 2
```
# socket module to import
import socket

# send something
send_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# where to send it to located
send_address = ('localhost', 10001)

# send an actual message
send_socket.sendto(b'hello from me', send_address)
```

terminal 1
```
print(result)
```

Connect to a webpage using urllib module

```
import urllib.request

url = 'https://www.robmiles.com/journal/rss.xml'
 
req = urllib.request.urlopen(url)
for line in req:
    print(line)
```    

Reading the current weather from a website with a small python program

```
import urllib.request
import xml.etree.ElementTree

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

```