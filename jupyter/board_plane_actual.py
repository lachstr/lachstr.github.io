import numpy as np
import random 

def last_passenger_sits_in_assigned_seat(plane_size, PRINT_EVENTS=False):
    
    plane = {}
    
    for seat_number in range(plane_size):
        plane[seat_number] = 'empty'
        
    passengers = [i for i in range(plane_size)]
    
    random.shuffle(passengers)
    
    
    ## Sit the first passenger in the wrong seat
    while (rand_seat := random.randint(0, plane_size-1)) == passengers[0]:
        pass
        ## Pick another random seat which isnt the assigned one

    plane[rand_seat] = 'taken'
    if (PRINT_EVENTS):
        print(f'Passenger {passengers[0]} sits in seat {rand_seat}')
    
    ## Seat the 2nd to 2nd last passengers according to logic above
    for passenger in passengers[1:-1]:
        if plane[passenger] == 'empty':
            ## This passenger can sit in their assigned seat
            if (PRINT_EVENTS):
                print(f'Passenger with seat {passenger} sits in their assigned seat')
            plane[passenger] = 'taken'
        else:
            ## Someone is sitting in this passenger's seat, find a random empty seat for them
            seats = list(plane.items())
            random.shuffle(seats)
            for seat_number, avaliability in seats:
                if avaliability == 'empty':
                    plane[seat_number] = 'taken'
                    if (PRINT_EVENTS):
                        print(f'Passenger with seat {passenger} sits in seat {seat_number}')
                    break
                    
    ## Check to see if the last passenger has thier seat
    if plane[passengers[-1]] == 'empty':
        return True
    else:
        return False

last_passenger_sits_in_assigned_seat(plane_size=10, PRINT_EVENTS=True)