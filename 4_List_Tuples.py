#['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
#('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
#'Hello World Huston we are here' -> 'World Huston we'

list = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
string = 'Hello World Huston we are here'

#1
print(list[1:5])
#2
print(list[:2])
#3
print(list[-2:])
print(list[-2:-1])
print(list[::2])
print(list[::-1])
print(list[1:-1])


names = ['George', 'Bejamin', 'Thomas', 'John']


#Claus, 51, male, clbo@kea.dk, 31011970-1313
#Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo
#Claus, Henning, Torben, Carl, Tine
#‘Hello’, ‘World’, ‘Huston’, ‘we’, ‘are’, ‘here’
#Rolling Stones, Goats Head Soup, 31 August 1973, 46:56
#40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan;

tup1 = ('Claus', 51, 'male', 'clbo@kea.dk', '31011970-1313')
li1 = ['Bmw', 'Toyota', 'Hyundai', 'Skoda', 'Fiat']
li2 = ['Claus', 'Henning', 'Torben', 'Carl', 'Tine']
li3 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
tup2 = ('Rolling Stones', 'Goats Head Soup', '31 August 1973', '46:56')


# sorted() - function, .sort() - method to sort a list, 

# methods changes the state of the object, they are for objects
# functions don't change the state of the object, they create a new object 


# list is a container type
# tuple is a record type

#Create a function that takes a string as a parameter and returns a list.
#The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

def sort_consonants(string):
    vowels = "aeiouAEIOU"
    consonants = [char for char in string if char not in vowels]
    sorted_consonants = sorted(consonants)
    return sorted_consonants

print(sort_consonants('elephant'))

# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# Sort this list by using the sorted() build in function.
# Sort the list in reversed order.
# Sort the list on the lenght of the name.
# Sort the list based on the last letter in the name.
# Sort the list with the names where the letter ‘a’ is in the name first.

l = ['Claus', 'Ib', 'Per', 'Adam']
sorted(l, reverse=True, key = len)
sorted(l, key = lambda x: x[-1])

print(sorted(l, key=lambda x: x.find('a')))

# Count the number of characters including blank spaces.
# Count the number of characters excluding blank spaces.
# Count the number of words.

s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
sim = 'heloo world'
print(len(s))

print(len(s)- s.count(' '))

list = s.split(' ')
print(len(list))

# Create a file and call it lyrics.txt (it does not need to have any content)
# Create a new file and call it songs.docx and in this file write 3 lines of text to it.
# open and read the content and write it to your terminal window. * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

# Open file in write mode
f = open('lyrics.txt', 'w')
file = open('songs.docx', 'w')
file.write('This is just a sample text that could have been a million times longer.\nThis is just a sample text that could have been a million times longer.\nThis is just a sample text that could have been a million times longer.')
file.close()

# Open file in read mode
fileToRead = open('songs.docx', 'r')
contents = fileToRead.read()
print(contents)
fileToRead.close()

fileToRead = open('songs.docx', 'r')
line = fileToRead.readline()
print(line)
fileToRead.close()


# with statement automatically closes the file 
with open("songs.docx", "r") as file:
    contents = file.read()
    print(contents)

fileToRead = open('songs.docx', 'r')
lines = fileToRead.readlines()
print(lines)
fileToRead.close()


# Ex 5: Sort a list of tuples

tuples = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
print(sorted(tuples, key=lambda x: (x[1], x[0])))

