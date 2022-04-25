# patrick notes program

from BTCInput import * 

tickets=[]

class Ticket:
    pass



def new_ticket(): 
    print('Create new ticket')
    new_ticket = Ticket()
    new_ticket.number = read_int('Enter the ticket number: ')
    new_ticket.description = read_text('Enter the ticket description: ')
    # add to the tickets list
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






menu='''Patrick ticket notes

1. New Ticket
2. Display Ticket
3. Edit Ticket
4. Exit program

Enter your command: '''

while True:
    command=read_int_ranged(prompt=menu,min_value=1,max_value=4)
    if command==1:
        new_ticket()
    elif command==2:
        display_ticket()
    elif command==3:
        edit_ticket()
    elif command==4:
        break
