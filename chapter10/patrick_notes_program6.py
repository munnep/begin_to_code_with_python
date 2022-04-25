# patrick notes program

from BTCInput import * 
import pickle




class Ticket:
    def __init__(self, number, description='default: no description'):
        self.number=number
        self.description=description
        



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
    else: 
        print('This ticket was not found.')

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
3. Edit Ticket
4. Exit program

Enter your command: '''

file_name='tickets.pickle'

try:
    load_tickets(file_name)
except:
    print('Tickets file not found') 
    tickets=[]
while True:
    command=read_int_ranged(prompt=menu,min_value=1,max_value=4)
    if command==1:
        new_ticket()
    elif command==2:
        display_ticket()
    elif command==3:
        edit_ticket()
    elif command==4:
        try:
            save_tickets(file_name)
        except:
            print('something went wrong during the saving. You lost data')
        break
