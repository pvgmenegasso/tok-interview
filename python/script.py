'''
This module reads a filename, a number N and returns a N-Gram.

Usage: python3 script.py filename N

'''
import sys

from objects.ngram import *

'''
====================================
||                                ||
||  FUNCTION DEFINITIONS          ||
||                                ||
====================================
'''



def getWords(fileName : str):
    
    '''Return Words in a file in form of a list of strings.'''
    
    # String to store results
    result : list[str] = []
    temp = open(str(fileName)).readlines() # Return list of lines in string format
    
    # Go through each line and get words
    for lines in temp:
        words = lines.strip() # Remove whitespaces (leading and trailling)
        words = lines.split(' ') # Split words using space char as separator
        
        # Now append each word into result
        for word in words:
            result.append(word)
    
    # Return the result, a list of words in a file
    return result

def getColors():
    """
    
    Load colors file into memory.

    @return:
        color : dict

    KEYS:
        OKBLUE
        OKCYAN
        OKGREEN
        WARNING
        
    """
    
    colorArray = open("colors").readlines()
    colorDict = {}

    for line in colorArray:
        # Remember to remove spaces
        line = line.replace(' ', '')
        colorName = line.split("=")[0]
        colorCode = line.split("=")[1]
        colorDict[colorName] = colorCode

    return colorDict



def help():
    """Print help text."""
    print(getColors()["OKCYAN"])
    print("""\n
        this script generates an N-gram given a filename \n
        and a number N between 0 and number of words in file \n
        usage: \n
            script.py filename n \n
            \n
            to print this statement use help, h or -h \n
        """)


def nParamsCheck(nLen):
    """Check script standard Input."""
    if nLen < 3:
        print(getColors()["WHAT"])
        print("missing arguments !")
        help()
        exit()
    if sys.argv[1] in ("help","h","-h"):
        help()
        exit()


def fileName():
    """Return string containing name of input file."""
    return sys.argv[1]



'''
====================================
||                                ||
||  MAIN CODE BEGINS HERE         ||
||                                ||
====================================
'''

# BEGIN

# Calculate lenght of Stdin
nLen = len(sys.argv)
# Check if it's an acceptable length
nParamsCheck(nLen)

print("loading file... ", fileName())

# Load color for aesthetic purposes
print(getColors()["OKGREEN"])

# Get all words found on the file

words = getWords(fileName())


print('''
==========================================

        RESULTING N GRAM !!
        
-      -       -         -       -      -        -     -
''')

gramN = nGram(words, int(sys.argv[2]))
for item in gramN:
    print(item.getGram() + " = "+str(item.getCount()))

exit()
