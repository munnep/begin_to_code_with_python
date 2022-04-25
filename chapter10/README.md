# Chapter 10

A class is a user defined type. 
```
class Contact:
    
    min_session_length = 0.5                 <-- class data variables
    max_session_length = 3.5                 <-- class data variables
    
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.hours_worked = 0

    def get_hours_worked(self): 
        '''
        Gets the hours worked for this contact
        '''
        return self.hours_worked 

    def add_session(self, session_length): 
        '''
        Adds the value of the parameter
        onto the hours worked for this contact
        '''
        if session_length < Contact.min_session_length:
            return
        if session_length > Contact.max_session_length:
            return
        self.hours_worked = self.hours_worked + session_length 
```

A static method can be called directly. It is good for validating things.

You use a static method if you want to create a behavior that is independent of any instance of a class. The validate_session_length method is not attached to any Contact object because it “speaks for” the entire class.
```
class Contact:
    
    min_session_length = 0.5
    max_session_length = 3.5

    @staticmethod
    
    def validate_session_length(session_length):
        '''
        Validates a session length and returns
        True if the session is valid or False if not
        '''
        if session_length < Contact.min_session_length:
            return False
        if session_length > Contact.max_session_length:
            return False
        return True
    
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.hours_worked = 0

    def get_hours_worked(self): 
        '''
        Gets the hours worked for this contact
        '''
        return self.hours_worked 

    def add_session(self, session_length): 
        '''
        Adds the value of the parameter
        onto the hours worked for this contact
        '''
        if not Contact.validate_session_length(session_length):
            return
        self.hours_worked = self.hours_worked + session_length

print(Contact.validate_session_length(5))        
```
output:
```
False
```


Instead of returning False we could raise an exception
```
    def add_session(self, session_length):
        '''
        Adds the value of the parameter
        onto the hours spent with this contact
        Raises an exception if the session length is invalid
        '''
        if not Contact.validate_session_length(session_length): 
           raise Exception('Invalid session length')                           # RAISE THE EXCEPTION
        self.hours_worked = self.hours_worked + session_length
```

Programmers should prefer to make exceptions that crashes the program then make the user think that everything worked without issues. 

the @property adds a property to a value
```
    __min_text_length = 4

    @staticmethod
    def validate_text(text):
        '''
        Validates text to be stored in the contact
        storage.
        True if the text is valid, false if not
        '''
        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not Contact.validate_text(name):
            raise Exception('Invalid name')
        self.__name = name
```
The code above shows how we would implement a property for the name value in the Contact class. The property performs validation and will reject an attempt to set the name of a string to fewer than four characters.  

Use the __str__ to retun a default for a class

```
    def __str__(self):
        template = '''Name: {0}
Address: {1}
Telephone: {2}
Hours on the case: {3}
Amount to bill: {4}
Sessions
{5}
'''
        return template.format(self.name, self.address, self.telephone,
                          self.hours_worked, self.billing_amount,
                               self.session_report)
```

Use it at a later point where ticket is the class which looks at __str__
```
 print(ticket)
```