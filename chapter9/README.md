# Chapter 9

remove any ny whitespace from around the name
```
name=name.strip()
```
convert the name to lower case
```
name = name.lower()
```
see if the names match
```
if name.startswith(search_name):
```

## class

```
class Contact:
pass
```
name should start with a Captital letter


open somethine as a binary file
```
output_file = open('contacts.pickle','wb')
```

initialize a class
```
>>> class InitPrint:
            def __init__(self):
                print('you made an InitPrint instance')
```
```
>>> x=InitPrint()
you made an InitPrint instance
```

dictionary
```
prices={'latte': 3.6, 'espresso': 3.0, 'tea': 2.5, 'americano':2.5}
```
```
>>> prices['latte']
3.6
```