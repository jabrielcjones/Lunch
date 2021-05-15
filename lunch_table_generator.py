#!/usr/bin/env python3

import random
import sys


def display_guest_list(guests, seats, prev_attendees_file):
    '''
    '''

    print('Printing out {0} guests for {1} seats'.format(len(guests), seats))
    print('=======================================')

    if len(guests) == 0:
        print('No new guests available.')
        print('=======================================')

    else:
        for guest in guests:
            print(guest + ';')

        print('=======================================')

        update_previous_attendees_list(guests, prev_attendees_file)


def get_potential_guests(emails_file):
    '''
    '''

    potential_guests = []

    with open(emails_file, 'r') as emails:
        for email in emails:
            email = email.split()
            email[2] = email[2][1:-2]
            potential_guests.append(email)

    return potential_guests


def get_previous_attendees(prev_attendees_file):
    '''
    '''

    previous_attendees = []

    with open(prev_attendees_file, 'r') as prev_attendees:
        for attendee in prev_attendees:
            # print(attendee.strip())
            previous_attendees.append(attendee.strip()[:-1])

    return previous_attendees


def create_short_list(potential_guest_emails, previous_attendees):
    '''
    Create a short list of potential guests who are not on the previous attendees list
    '''

    return list(set(potential_guest_emails) - set(previous_attendees))


def create_guest_list(short_list, seats):
    '''
    '''

    guests = []

    if len(short_list) < int(seats):
        guests = short_list

    else:
        while len(guests) < int(seats):
            candidate = random.choice(short_list)

            if candidate not in guests:
                guests.append(candidate)

    return guests


def update_previous_attendees_list(guests, prev_attendees_file):
    '''
    '''

    with open(prev_attendees_file, 'a') as prev_attendees:
        for guest in guests:
            prev_attendees.write(guest + ';\n')

    print('Attendees List Updated: {}'.format(prev_attendees_file))


if __name__ == "__main__":
    '''
    '''

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

    potential_guests = get_potential_guests(emails_file)

    previous_attendees = get_previous_attendees(prev_attendees_file)

    potential_guest_emails = [guest[2] for guest in potential_guests]

    short_list = create_short_list(potential_guest_emails, previous_attendees)

    guests = create_guest_list(short_list, seats)

    display_guest_list(guests, seats, prev_attendees_file)
