# Chapter 12: Python applications

A function takes something, does something with it, and then returns a result. You can think of a lambda expression as a tiny function that we can write on one line.

python function
```
def increment(x):
    return x+1
```

the same as lambda expression
```
increment = lambda x : x+1

>>> increment(5)
6
```

example:
```
numbers = [1,2,3,4,5,6,7,8]

def increment(x):
    return x+1

new_numbers = map(increment, numbers)
```

with lambda
```
new_numbers = map(lambda x : x+1, numbers)
```

yield
```
def mr_yield():
        yield 1
        yield 2
        yield 3
        yield 4

for i in mr_yield():
    print(i)

1
2
3
4
>>> list(mr_yield())
[1, 2, 3, 4]

```


an arbitrary number of values to a function

```
def add_function(*values):
    total = 0
    for value in values:
        total = total + value
    return total
```

We stored the program code for functions in a file called BTCInput.py. Programs that wanted to use these functions had to import that BTCInput file to use them. In Python, these files are called modules

The _init_.py file provides a way for a programmer to gain control when a package is loaded. The Python statements in the __init__.py are obeyed when the package folder is first opened. You can think of this as an initializer for packages. The __init__.py file can set up resources and could contain a help string that describes the package contents.


Python provides a language construction called assert that programs can use to test themselves as they run. In English, the word “assert” means “stating firmly something that you believe to be true .” I

```
item = StockItem(stock_ref='Test', price=10, tags='test:tag')
assert item.stock_level == 0
```

assert can be done manually to test things but there is a framework for unittests

```
import unittest
```

Generate documentation of you programs using pydoc with output of a webpage

```
python3 -m pydoc -b
```