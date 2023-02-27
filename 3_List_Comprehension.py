


#Create a list of capital letters in the english alphabet
capital_letters = [chr(letter) for letter in range(65, 91)]
print(capital_letters)
#Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
excluded_code_points = {70, 75, 80, 85}
capital_letters = [chr(letter) for letter in range(65, 91) if letter not in excluded_code_points]
print(capital_letters)
#Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
capital_letters = [chr(letter) for letter in range(65, 91) if letter < 70 or letter > 79 or letter % 2 == 1]
print(capital_letters)

#From 2 lists, using a list comprehension, create a list containing:
#[(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

#If the tuple pair is in the following list, it should not be added to the comprehension generated list.
#sold_out = [('Black', 'm'), ('White', 's')]
result = [(color, size) for color in colors for size in sizes]
sold_out = [('Black', 'm'), ('White', 's')]
result2 = [(color, size) for color in colors for size in sizes if (color, size) not in sold_out]

#Create a list of even numbers from 0 to 20.
numbers = [number for number in range(0, 21) if number % 2 == 0]
print(numbers)
#Create a list of squares of numbers from 1 to 10.
squares = [(x * x) for x in range(1, 11)]
print(squares)

#Create a list of all the vowels in a given string.
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def vowelsString(string):
    vowelsInString = [vowel for vowel in string if vowel in vowels]
    return vowelsInString

print(vowelsString('Simona'))

#Create a list of common elements in two given lists.

def commonElements(list1, list2):
    elements = [el for el in list1 if el in list2]
    return elements

print(commonElements([2,3,4,5], [3, 4, 6]))

#Create a list of words from a given string that have more than 4 letters.

def longWords(string):
    words = string.split() 
    long_words = [word for word in words if len(word) > 4]
    return long_words

print(longWords('Hello, my name is Simona and I am learning Python'))
