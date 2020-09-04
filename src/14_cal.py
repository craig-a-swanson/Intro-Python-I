"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime, date

# count the number of aruments passed in
# if that number is zero, print the current month
# if that number is one, print that month for the current year
# if that number is two, print that month for that year
# else, print a message with the expected format
arg_number = len(sys.argv)

cal = calendar.TextCalendar()
curr_date = date.today()

if arg_number == 1:
    # print current month
    cal.prmonth(2020, curr_date.month)
elif arg_number == 2:
    # print arg month for current year
    passed_month = sys.argv[1]
    cal.prmonth(curr_date.year, int(passed_month))
elif arg_number == 3:
    # print arg1 month for arg2 year
    passed_month = sys.argv[1]
    passed_year = sys.argv[2]
    cal.prmonth(int(passed_year), int(passed_month))
else:
    # print error message
    print("Please use format: 14_cal.py [month] [year]\n"
    "example: 14_cal.py 3 1999")
