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

def find_ticket(): 
    print('Find ticket')
    search_ticket = read_int('Enter the ticket number: ')
    
    result = None
    print(result)
    for ticket in tickets:
        if ticket.number == search_ticket:
            # print('search_ticket: ', search_ticket)
            # print('ticket: ', ticket.number)
            result = ticket
            # print('result: ', result.number)
            break
        

    if result != None:
        print('ticket:', result.number)
        print('description:', result.description)
    else: 
        print('This ticket was not found.')

menu='''Patrick ticket notes

1. New Ticket
2. Find Ticket
3. Exit program

Enter your command: '''

while True:
    command=read_int_ranged(prompt=menu,min_value=1,max_value=3)
    if command==1:
        new_ticket()
    elif command==2:
        find_ticket()
    elif command==3:
        break
