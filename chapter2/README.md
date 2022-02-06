# Chapter 2: Python and Programming

functional design specification --> FDS
Developer and customer both agree on what to build

prototyping
Making a series of solutions and discussing this with the customer

operand -> Thing to work on
operator -> thing to do

substract strings is not possible
```
>>> 'hello' + ' world'
'hello world'
>>> 'hello' - 'o'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

adding doesn't work but multiply does. 
```
>>> 'hello' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'hello' * 2
'hellohello'
```


## functions
The ```ord``` function takes a Character and returns the integer number
```
>>> ord('W')
87
```
ord -> function
'W' -> argument

other way around. ```chr``` function takes a integer and represents string value
```
>>> chr(87)
'W'
```
 The bin function takes a number and returns a string of bits that rep- resents the value of that number.

```
>>> bin(87)
'0b1010111'
>>> bin(ord('W'))
'0b1010111'
```