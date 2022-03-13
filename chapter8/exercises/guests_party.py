# guests_at_party

#fetch the input functions
from BTCInput import *  

#create an empty guests list
guests=[]

number_guests=read_int('How many guests do you expect? ')

# read in 10 sales figures 
for count in range(1,number_guests+1):
    # assemble a prompt string
    prompt='Enter the names of the guests: '
    # read a value and append it to sales array
    guests.append(read_text(prompt))

# print a heading
print('Guest list')

count = 1
# work through the guests figures and print them
for guest_value in guests:
    # print an item
    print('Guest number', count,'is',guest_value)
    # advance the stand counter
    count = count + 1         
