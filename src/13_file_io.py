"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

foo_file = open('foo.txt', 'r')
print(foo_file.read())
foo_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar_file = open('bar.txt', 'w')
bar_file.write('Line one\nLine two\nLine three')
bar_file.close()

bar_file = open('bar.txt', 'r')
print(bar_file.read())
bar_file.close()
