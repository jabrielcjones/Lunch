# Lunch Problem

Add write permissions
```
chmod +x lunch_table_generator
```

Run solution
```
./lunch_table_generator
```

## Problem Statement

I have a lunch table.
I want to have new randomly-selected people at this table each lunch.
I do not want people who previously attended.

Write a program that takes a number of availible seats, a list of all emails, a list of all previous attendees as inputs.
Generate a random list of N people to attend my lunch table and update the previous attendee list.
Please follow the expected output


## Expected Usage

java LunchTableGenerator <num_seats> <file_all_emails> <file_prev_attended>

## Expected Output

Please match the example output format

## Details
- Use the attached sampleemails.txt for all_emails

- The program will only print out the output as defined below

- The program will keep track of all previous guests in <file_prev_attended>

- Input files provided should be parsed in a newline insensitive manner.

- Emails should be case-insensitive

## Grading

We will go over your solution together during the interview.

Programs will be judged on the following criteria:

	# Logical Correctness
		- Does the program fulfill the requirements?
		- Are edge cases considered?
	# Error Handling
		- Have you considered how the program could throw errors?
		- It is okay to use System.exit or throw an exception.
	# Code Quality
		- Is the code well-organized,concise

This is your chance to shine, please show us your best work.
This is "open book", but please share any resources that you used. 

Time Expected for New Grads: 2 hours

## Example Output

$ java LunchTableGenerator 10 all_emails.txt prev_attendees.txt
Printing out 10 attendee list
=======================================
first.last10@swift.com;
first.last11@swift.com;
first.last12@swift.com;
first.last13@swift.com;
first.last14@swift.com;
first.last15@swift.com;
first.last16@swift.com;
first.last17@swift.com;
first.last18@swift.com;
first.last19@swift.com;
=======================================
Attendees List Updated: [prev_attendees.txt]

$ java LunchTableGenerator 5 all_emails.txt prev_attendees.txt
Printing out 5 attendee list
=======================================
first.last1@swift.com;
first.last2@swift.com;
first.last3@swift.com;
first.last4@swift.com;
first.last5@swift.com;
=======================================
Attendees List Updated: [prev_attendees.txt]

$ java LunchTableGenerator 5 all_emails.txt prev_attendees.txt
Printing out 5 attendee list
=======================================
first.last1@swift.com;
first.last2@swift.com;
All Employees Attended
=======================================
Attendees List Updated: [prev_attendees.txt]
