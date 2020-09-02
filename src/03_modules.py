"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for index, arg in enumerate(sys.argv):
    print(f"{index}: {arg}")
    

# Print out the OS platform you're using:
print(f"My system platform is {sys.platform}")

# Print out the version of Python you're using:
print(f"My Python interpreter is version {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

# Print the current working directory (cwd):
# YOUR CODE HERE

# Print out your machine's login name
# YOUR CODE HERE
