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

class romanNumeralTranslator():
    #this function will translate a roman numeral into a modern numeral
    #if the roman numearl given is not a real roman numeral it will return -1
    def translateToNow(roman = 'DEFAULT'):
        #dictionary with the key for roman numeral letters
        #tupal contains (modern numerical value, x from 10^x)
        key = {'I':(1, 0), 'V':(5, 0), 'X':(10,1), 'L':(50, 1), 
               'C':(100, 2), 'D':(500, 2), 'M':(1000, 3), '!':(0,0)}
        
        #checks the user input for invalid letters
        for letter in roman:
            if letter not in key:
                return -1
        
        #The modern numercial value of the user's roman numeral
        modern = 0
        #flag is used to keep track of when subtractive notation is applied
        flag = False
        #adds '!' to end of roman string
        roman = roman + '!'
        
        #for loop checks other roman numeral requirements and calculates
        #the modern numerical equivilent
        indexCount = 0
        for letter in roman:
            #checks for the last index to avoid out of range errors
            if letter != '!':    
                #checks if the value of letter is too small to proceed the next value
                if (key[roman[indexCount + 1]][1] - key[letter][1]) >= 2:
                    return -1
                #catches subtractive notation flag
                elif flag:
                    #applys subtractive notation to the current letter 
                    #(current - previous)
                    modern += (key[letter][0] - key[roman[indexCount - 1]][0])
                    flag = False
                #checks if current letter is the first in a 
                #"subtractive notation" pair
                elif key[roman[indexCount + 1]][0] > key[letter][0]:
                    flag = True
                else:
                    modern += key[letter][0]
            indexCount += 1
        return modern;
    
    """
    def translateToRome(num = 0):
        num = int(num)
        rome = ''
        if num / 1000 > 0:
            rome += 'M'
            num = num % 1000
            rome += self.translateToRome(num)
        elif num / 900 > 0:
            rome += 'CM'
            num = num % 900
            rome += self.translateToRome(num)
        elif num / 500 > 0:
            rome += 'D'
            num = num % 500
            rome += self.translateToRome(num)
        elif num / 400 > 0:
            rome += 'CD'
            num = num % 400
            rome += self.translateToRome(num)
        elif num / 100 > 0:
            rome += 'C'
            num = num % 100
            rome += self.translateToRome(num)
        elif num / 90 > 0:
            rome += 'XC'
            num = num % 90
            rome += self.translateToRome(num)
        elif num / 50 > 0:
            rome += 'L'
            num = num % 50
            rome += self.translateToRome(num)
        elif num / 40 > 0:
            rome += 'XL'
            num = num % 40
            rome += self.translateToRome(num)
        elif num / 10 > 0:
            rome += 'X'
            num = num % 10
            rome += self.translateToRome(num)
        elif num / 9 > 0:
            rome += 'IX'
            num = num % 9
            rome += self.translateToRome(num)
        elif num / 5 > 0:
            rome += 'V'
            num = num % 5
            rome += self.translateToRome(num)
        elif num / 4 > 0:
            rome += 'IV'
            num = num % 4
            rome += self.translateToRome(num)
        elif num / 1 > 0:
            rome += 'I'
            num = num % 1
            rome += self.translateToRome(num)
        else:
            rome = ''
        return rome;
    """
    
    #Gets the numeral from the user    
    userInput = input("Enter the numeral: ")
    
    translation = None
    
    """
    #calls the correct of the two translation functions
    #if type(userInput) == str:
        #translation = translateToNow(userInput)
    if int(userInput) >= 0:
        translation = translateToRome(userInput)
    else:
        translation = translateToNow(userInput)
    """
        
    translation = translateToNow(userInput)
    
    #checks to see if translateToNow returned -1 (false user input)
    if(translation == -1):
        print(userInput + " is not a roman numeral.")
    else:
        print(userInput + " is: " + str(translation))
                