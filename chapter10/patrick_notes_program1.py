# patrick notes program

from BTCInput import * 

tickets=[]
description=[]



def new_ticket(): 
    print('Create new ticket')
    tickets.append(read_int('Enter the ticket number: '))
    description.append(read_text('Enter the ticket description: '))

def find_ticket(): 
    print('Find ticket')
    search_ticket = read_int('Enter the ticket number: ')
    ticket_index=0
    for ticket in tickets:
        if ticket == search_ticket:
            break
        ticket_index = ticket_index + 1

    if ticket_index < len(tickets):
        print('ticket:', tickets[ticket_index])
        print('description:', description[ticket_index])
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
