# Modules
# - can be written in Python itself
# - can be written in C and loaded dynamically at run-time
# - build-in module are contained in the interpreter (Random, DateTime ..)

#CREATE YOUR OWN MODULE
string = 'Computers are useless. They can only give you answers.'
list = [100, 200, 300]

def printY(arg):
    print(f'arg = {arg}')

class Classy:
    pass


# Importing a module
# The interpreter searches for the file:
# - in the current directory
# - in the PYTHONPATH environment variable list of directories
# - in the directories configures as part of the python installation

# sys module
# sys.path - to see where modules can be imported from
# sys.path.append(r'directory path') - to add path (lasts only one session)

# Import statement
# import module
# from module import string
# import module as my_module
# from module import string as s, list as l

