# Chapter 5

If satement
```
if hour > 6:
    print('IT IS TIME TO GET UP')
    print('THE EARLY BIRD GETS THE WORM')
```

could be the same as this. Don't use this format
```
if hour > 6:print('IT IS TIME TO GET UP');print('THE EARLY BIRD GETS THE WORM')
```

Nested if confidition
```
name = input('Enter your name: ')

if name.upper() == 'ROB':
    password = input('Enter the password: ')
    if password == 'secret':
        print('Hello, Oh great one')
else:
    print('You are not Rob. Shame.')
```