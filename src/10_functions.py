# Write a function is_even that will return true if the passed-in number is even.

def is_even(number_to_check):
    if number_to_check % 2 == 0:
        return True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num):
    print("Even!")
else:
    print("Odd")
