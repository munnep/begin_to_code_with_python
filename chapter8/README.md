# chapter 8

list
```
sales=[]
```

data
```
sales=[1,5,7]
```
sort data
```
sales.sort()
```

write to a file
```
output_file=open('test.txt','w')
output_file.write('First line\n')
output_file.write('Second line\n')
output_file.close()   
```
append to a file
```
output_file=open('test.txt','a')
output_file.write('First line\n')
output_file.write('Second line\n')
output_file.close()   
```


read a file
```
input_file=open('test.txt','r')
```

finally will always be done
```
try:
    output_file=open(file_name,'w')
    for sale in sales:
        output_file.write(str(sale)+'\n')
except:
    print('Something went wrong writing the file')
finally:
    output_file.close()
```


day names
```
day_names=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day_name=day_names[day_number]
```