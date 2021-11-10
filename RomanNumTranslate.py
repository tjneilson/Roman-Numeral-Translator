"""
Created on Mon Dec 28 20:43:38 2020

@author: tjnei

This script is inteded to be run in the command line

it will ask the user:
    "Enter the numeral: "
and then print
    "[user input] is: [the translation]"

if the user inputs something that is not a roman numeral and not a modern number
it will print
    "[user input] is not a roman numeral"
"""

# this function will translate a roman numeral into a modern numeral
# if the roman numearl given is not a real roman numeral it will return -1
def translateToNow(roman = 'DEFAULT'):
    # defines a dictionary for roman numeral letters and assositated modern value
    key = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    # checks the user input for invalid letters
    for letter in roman:
        if letter not in key:
            return -1

    # the modern numercial value of the user's roman numeral
    modern = 0
    # flag is used to keep track of when subtractive notation is applied
    flag = False
    # adds '!' to end of roman string
    roman = roman + '!'
    # adds a key value of '!'
    # done after the invalid letters test to avoid users adding '!' to input
    key['!'] = 1

    # for loop checks other roman numeral requirements and calculates
    # the modern numerical equivilent
    indexCount = 0
    for letter in roman:
        # checks for the last index to avoid out of range errors
        if letter != '!':
            # checks if the value of letter cannot proceed the next value
            test = key[roman[indexCount + 1]] / key[letter]
            if test > 10 or test == 2:
                return -1
            # catches subtractive notation flag
            elif flag:
                # applys subtractive notation to the current letter
                # (current - previous)
                modern += (key[letter] - key[roman[indexCount - 1]])
                flag = False
            # checks if current letter is the first in a
            # "subtractive notation" pair
            elif key[roman[indexCount + 1]] > key[letter]:
                flag = True
            else:
                modern += key[letter]
        indexCount += 1

    return modern;

# This function translates a modern numeral into a roman numeral
def translateToRome(modern = 0):
    # defines a dictionary for the corusponding letters associated with
    # modern numberical values
    key = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC',
           50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

    # makes sure the user input is an integer
    modern = int(modern)
    # a string which will hold the translation into roman numerals
    rome = ''

    # this loop translates the number into roman numerals by finding the largest
    # roman numeral letter value in the modern number, recording that letter
    # and removing that numerical value and repeating until a full translation
    # is recorded
    for digit in key:
        while modern >= digit:
            rome = rome + key[digit]
            modern -= digit

    return rome;

# gets the numeral input from the user
userInput = input("Enter the numeral: ")
# defines a variable to hold the translation
translation = None

# program assumes the input is a modern numeral (an integer)
inputIsModern = True
# tests if the userInput can be translated to an integer. ]
# If it can not, then the program knows the input is a string
try:
    int(userInput)
    translation = translateToRome(userInput)
except:
    inputIsModern = False
    translation = translateToNow(userInput)

# checks to see if translateToNow returned -1 (invalid user input)
if(translation == -1):
    print(userInput + " is not valid input")
else:
    print(userInput + " is: " + str(translation))
