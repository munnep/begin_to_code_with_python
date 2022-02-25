# Functions

example:
```
 def greeter():
    print('Hello')
```

bigger example
```
# EG7-02 Times Table
def print_times_table(times_value):
    count = 1
    while count < 13:
        result = times_value * count
        print(count,'times', times_value,'equals',result)
        count = count + 1

print_times_table(6)

```

Storing global variables: it will print 100
```
cheese=99

def func():
    global cheese
    cheese=100
    print('Global cheese is:',cheese)

func()
print('Global cheese is:',cheese)
```

pydoc can be used to get the information from a function

```
import pydoc
pydoc.help(print)

```

What python calls a method other programming languages call it a library

Create file call BTCInput for example with all the functions

You can import it in you code in several ways
```
import BTCInput
age = BTCInput.read_float_ranged('Enter your age:', min_value=5, max_value=90)
```
or 
```
from BTCInput import read_float_ranged
age = read_float_ranged('Enter your age:', min_value=5, max_value=90)
```
or
```
from BTCInput import *
age = read_float_ranged('Enter your age:', min_value=5, max_value=90)
```