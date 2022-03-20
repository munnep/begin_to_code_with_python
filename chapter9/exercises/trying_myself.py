from BTCInput import *
import pickle

# Create the contact class

class Race:
    def __init__(self,track,date,time):
        self.track=track
        self.date=date
        self.time=time

def new_race():
    '''
    Reads in a new race and stores it
    '''
    print('Create new race')
    # add the data attributes
    track=read_text('Enter the race track: ')
    date=read_text('Enter the race date: ')
    time=read_text('Enter the race time: ')
    # create a new instance
    new_race=Race(track=track,date=date,time=time)
    # add the new contact to the contact list
    races.append(new_race)

def find_race(search_track):
    '''
    Finds the contact with the matching name
    Returns a contact instance or None if there is
    no contact with the given name
    '''
    # remove any whitespace from around the search name
    search_track = search_track.strip()
    # convert the search name to lower case
    search_track = search_track.lower()
    for race in races:
        # get the name out of the contact
        track=race.track
        # remove any whitespace from around the name
        track=track.strip()
        # convert the name to lower case
        track = track.lower()
        # see if the names match
        if track.startswith(search_track):
            # return the contact that was found
            return race
    # if we get here no contact was found
    # with the given name
    return None
    
def display_race():
    '''
    Reads in a name to search for and then displays
    the content information for that name or a
    message indicating that the name was not found
    '''
    print('Find race')
    search_track = read_text('Enter the race track: ')
    race=find_race(search_track)
    if race!=None:
        # Found a contact
        print('track: ',race.track)
        print('date: ',race.date)
        print('time: ',race.time)
    else:              
        print('This name was not found.')

def edit_race():
    '''
    Reads in a name to search for and then allows
    the user to edit the details of that contact
    If there is no contact the funciton displays a
    message indicating that the name was not found
    '''
    print('Edit race')
    search_track=read_text('Enter the race track:')
    race=find_race(search_track)
    if race!=None:
        # Found a race
        print('track: ',race.track)
        new_track=read_text('Enter new track or . to leave unchanged: ')
        if new_track!='.':
            race.track=new_track
        new_date=read_text('Enter new date or . to leave unchanged: ')
        if new_date!='.':
            race.date=new_date
        new_time=read_text('Enter new time or . to leave unchanged: ')
        if new_time!='.':
            race.time=new_time
    else:              
        print('This track was not found.')

def save_races(file_name):
    '''
    Saves the contacts to the given filename
    Contacts are stored in binary as pickled file
    Exceptions will be raised if the save fails
    '''
    print('save races')
    with open(file_name,'wb') as out_file:
        pickle.dump(races,out_file)

def load_races(file_name):
    '''
    Loads the contacts from the given filename
    Contacts are stored in binary as pickled file
    Exceptions will be raised if the load fails
    '''
    global races
    print('Load races')
    with open(file_name,'rb') as input_file:
        races=pickle.load(input_file)

menu='''Tiny F1 races

1. New race
2. Find race
3. Edit race
4. Exit program

Enter your command: '''

filename='racing.pickle'
try:
    load_races(filename)
except:
    print('Racing file not found')
    races=[]

while True:
    command=read_int_ranged(prompt=menu,min_value=1,max_value=4)
    if command==1:
        new_race()
    elif command==2:
        display_race()
    elif command==3:
        edit_race()
    elif command==4:
        save_races(filename)
        break
