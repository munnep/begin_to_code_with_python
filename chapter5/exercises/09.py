name = input('Enter your name: ')

if name.upper() == 'ROB':
    password = input('Enter the password')
    if password =='secret':
        print('Hello, Oh great one')
else:
    print('You are not Rob. Shame.')
