#!/usr/bin/env python3

import random
import sys

if __name__ == "__main__":
    '''
    '''

    # Handle arguments

    try:
        seats = sys.argv[1]
        emails_file = sys.argv[2]
        prev_attendees_file = sys.argv[3]

    except IndexError:
        print('ERROR: missing arguments')
        print('lunch_table_generator <num_seats> <file_all_emails> <file_prev_attended>')
        exit()

    except Exception as e:
        print('ERROR: {}'.format(e))
        exit()

    # Extract data from files
    potential_guests = []
    previous_attendees = []

    with open(emails_file, 'r') as emails, open(prev_attendees_file, 'r') as prev_attendees:
        for email in emails:
            email = email.split()
            email[2] = email[2][1:-2]
            potential_guests.append(email)

        for attendee in prev_attendees:
            # print(attendee.strip())
            previous_attendees.append(attendee.strip()[:-1])

    # Use seat count to define sample space
    # Generate a list of unique random numbers equal to seat count
    guests = []

    potential_guest_emails = [guest[2] for guest in potential_guests]
    # previous_attendees_emails = [prev_attendee for prev_attendee in previous_attendees]

    short_list = list(set(potential_guest_emails) - set(previous_attendees))

    if len(short_list) < int(seats):
        guests = short_list

    else:
        while len(guests) < int(seats):
            candidate = random.choice(potential_guest_emails)

            # if candidate not in guests and candidate not in previous_attendees:
            if candidate not in guests:
                guests.append(candidate)

    print('Printing out {} attendee list'.format(seats))
    print('=======================================')

    if len(guests) == 0:
        print('No new guests available.')
        print('=======================================')

    else:
        for guest in guests:
            print(guest + ';')

        print('=======================================')

        with open(prev_attendees_file, 'a') as prev_attendees:
            for guest in guests:
                prev_attendees.write(guest + ';\n')

        print('Attendees List Updated: {}'.format(prev_attendees_file))
