# Chapter 11: Object-based solution design

It would make sense to create a class to hold each kind of data we wish to store. Programmers call this object-oriented programming. The idea is that elements in a solution are represented by software “objects.” The first step in creating an application is to identify these objects.

Inheritance lets us base one class on an existing superclass. 

In Python terms, inheritance means the attributes a subclass gets from its superclass. Some programmers call the superclass the parent class and the subclass the child class.

example class with subclass
```
class StockItem(object):
    '''
    Stock item for the fashion shop
    '''

    def __init__(self, stock_ref, price, color):
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.color = color

    @property
    def price(self):
        return self.__price

    @property
    def stock_level(self):
        return self.__stock_level


class Dress(StockItem):

    def __init__(self, stock_ref, price, color, pattern, size):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.pattern = pattern
        self.size = size

x = Dress(stock_ref='D001', price=100, color='red', pattern='swirly', size=12)
print(x.pattern)
print(x.price)
```

Polymorphism
Overriding the __str__ method in a class is a great example of polymorphism at work.

extra logging:

example add this to a class
```
   show_instrumentation = True

    def __init__(self, stock_ref, price, color, location):
        if StockItem.show_instrumentation:
            print('** StockItem __init__ called')
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.StockItem_version = 1
        self.color = color
        self.location = location
```

Python sets
Python lets us create variables that can hold sets of data. A set is a collection of values. However, unlike a list, each value in a set is unique.

```
>>> set2={2,3,4,5}
>>> set2
{2, 3, 4, 5}
>>> set2.add(6)
>>> set2
{2, 3, 4, 5, 6}
>>> set2.add(3)
>>> set2
{2, 3, 4, 5, 6}
```