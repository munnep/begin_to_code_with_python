# patrick notes program

from BTCInput import * 
import pickle
import time


class Session:
    
    __min_session_length = 0.5
    __max_session_length = 4.0
   
    @staticmethod
    def validate_session_length(session_length):
        '''
        Validates a session length and returns
        True if the session is valid or False if not
        '''
        if session_length < Session.__min_session_length:
            return False
        if session_length > Session.__max_session_length:
            return False
        return True

    def __init__(self, session_length):
        if not Session.validate_session_length:
            raise Exception('Invalid session length')
        self.__session_length = session_length
        self.__session_end_time = time.localtime()
        self.__version = 1

    @property
    def session_length(self):
        return self.__session_length

    @property
    def session_end_time(self):
        return self.__session_end_time

    def check_version(self):
        pass
    
    def __str__(self):
        template = 'Date: {0} Length: {1}'
        date_string = time.asctime(self.__session_end_time)
        return template.format(date_string, self.__session_length)

class Ticket:

    hours_minimum = 0.5
    hours_maximum = 4.0

    __valid_text_length = 4

    def __init__(self, number, description='default: no description'):
        self.number=number
        self.description=description
        self.__hours=0
        self.__sessions = []
        self.__version=3

    def __str__(self):
        template = '''
Ticket number: {0}
Description: {1}
Hours worked: {2}
Sessions: {3}
        '''
        return template.format(self.number, self.description,self.__hours,self.session_report)    

    def check_version(self):
        if self.__version == 1:
             self.__version=2
        
        if self.__version == 2:
            self.__sessions = []
            self.__version = 3

        for session in self.__sessions:
            session.check_version()    

     
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,description):
        if not Ticket.validate_text(description):
            raise Exception('Invalid description')
        self.__description=description    


    @staticmethod
    def validate_hours(add_hours):    
        if add_hours < Ticket.hours_minimum:
            return False
        if add_hours > Ticket.hours_maximum:
            return False
        return True    
    
    @staticmethod
    def validate_text(text):    
        if len(text) < Ticket.__valid_text_length:
            return False
        else:
            return True    


    def get_hours(self):
        '''
        how many hours have worked
        '''
        return self.__hours

    # def add_hours(self, add_hours):
    #     '''
    #     how many hours have worked
    #     '''
    #     if not Ticket.validate_hours(add_hours):
    #         raise Exception('wrong number of hours')
    #     self.__hours = self.__hours + add_hours

    def add_session(self, session_length):
        '''
        Adds the value of the parameter
        onto the hours spent with this contact
        Raises an exception if the session length is invalid
        '''
        if not Session.validate_session_length(session_length): 
           raise Exception('Invalid session length')
        self.__hours = self.__hours + session_length
        session_record = Session(session_length)
        self.__sessions.append(session_record)

    @property
    def session_report(self):
        # Convert the list of sessions into a list of strings
        report_strings=map(str,self.__sessions)
        # Convert the list of strings into one string
        # separated by newline characters
        report_result = '\n'.join(report_strings)
        return report_result        

        

def new_ticket(): 
    print('Create new ticket')
    number = read_int('Enter the ticket number: ')
    description = read_text('Enter the ticket description: ')
    # add to the tickets list
    new_ticket = Ticket(number=number, description=description)
    tickets.append(new_ticket)

def find_ticket(search_number): 
    
    for ticket in tickets:
        if ticket.number == search_number:
            # print('search_ticket: ', search_ticket)
            # print('ticket: ', ticket.number)
            return ticket
    return None    


def display_ticket(): 
    ticket = find_ticket(read_int('Enter the ticket number: '))

    if ticket != None:
        print(ticket)
    else: 
        print('This ticket was not found.')


def display_all_ticket(): 
    for ticket in tickets:
        print('=================')
        print('ticket number used: ', ticket.number)
        print('Ticket description: ', ticket.description)        
        print('=================')

def edit_ticket(): 
    result = find_ticket(read_int('Enter the ticket number: '))
        
    if result != None:
        print('ticket:', result.number)
        print('Current description:', result.description)
        new_description = read_text('Enter the new description or . to leave the same: ')
        if new_description == '.':
            print('nothing to change')
        else:
            result.description = new_description
    else: 
        print('This ticket was not found.')

def add_hours_to_ticket(): 
    ticket = find_ticket(read_int('Enter the ticket number: '))
        
    if ticket != None:
        # Found a contact
        print('Ticket: ',ticket.number)
        print('Previous hours worked:',ticket.get_hours())
        add_hours=read_float(prompt='Adding hours: ')
        try:
            ticket.add_session(add_hours)
            print('Updated hours worked:', ticket.get_hours())
        except Exception as e:
            print('add Failed:', e)
    else:              
        print('This name was not found.')      

def save_tickets(file_name):
    '''
    Saves the tickets to the given file name
    Tickets are stored in binary as a pickled file
    Exceptions will be raised if the save fails
    '''
    print('save tickets')
    with open(file_name,'wb') as out_file:
        pickle.dump(tickets,out_file)

def load_tickets(file_name):
    '''
    Loads the contacts from the given file name
    Contacts are stored in binary as pickled file
    Exceptions will be raised if the load fails
    '''
    global tickets
    print('Load tickets')
    with open(file_name,'rb') as input_file:
        tickets=pickle.load(input_file)
    for ticket in tickets:
        ticket.check_version()    



menu='''Patrick ticket notes

1. New Ticket
2. Display Ticket
3. Display All Tickets
4. Edit Ticket
5. Add hours to Ticket
6. Exit program

Enter your command: '''

file_name='tickets.pickle'

try:
    load_tickets(file_name)
except:
    print('Tickets file not found') 
    tickets=[]
while True:
    command=read_int_ranged(prompt=menu,min_value=1,max_value=6)
    if command==1:
        new_ticket()
    elif command==2:
        display_ticket()
    elif command==3:
        display_all_ticket()
    elif command==4:
        edit_ticket()
    elif command==5:
        add_hours_to_ticket()
    elif command==6:
        try:
            save_tickets(file_name)
        except:
            print('something went wrong during the saving. You lost data')
        break
