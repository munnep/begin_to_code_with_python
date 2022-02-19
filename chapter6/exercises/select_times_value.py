# EG6-09 Times Table Tutor
count = 1
timesValue_string = input('Which value do you want to multiple?')
timesValue = int(timesValue_string)
while count < 13:
    result = count * timesValue
    print(count,'times',timesValue,'equals',result)
    count = count + 1; 
