# patrick notes program

from BTCInput import * 
import pickle




class Ticket:

    hours_minimum = 0.5
    hours_maximum = 4.0

    __valid_text_length = 4

    def __init__(self, number, description='default: no description'):
        self.number=number
        self.description=description
        self.__hours=0
     
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

    def add_hours(self, add_hours):
        '''
        how many hours have worked
        '''
        if not Ticket.validate_hours(add_hours):
            raise Exception('wrong number of hours')
        self.__hours = self.__hours + add_hours
        

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
    result = find_ticket(read_int('Enter the ticket number: '))

    if result != None:
        print('ticket:', result.number)
        print('description:', result.description)
        print('hours worked:', result.get_hours())
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
            ticket.add_hours(add_hours)
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
