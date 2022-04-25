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