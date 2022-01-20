"""This module reads a filename, a number N and returns a N-Gram."""
import sys



'''
====================================
||                                ||
||  FUNCTION DEFINITIONS          ||
||                                ||
====================================
'''

def getWords(fileName : str):
    '''Return Words in a file in form of a list of strings
    '''
    result : [str] = []
    temp = open(str(fileName)).readlines() # Return list of string containing the lines
    for lines in temp:
        words = lines.strip() # Remove whitespaces (leading and trailling)
        words = lines.split(' ') # Split words using space char as separator
        # Now append each word into result
        for word in words:
            result.append(word)
            
    return result


def nGram(numberN, listOfWords):
    '''Given a number N return a Ngram from a given a list of words
    
    @PARAMS:
        numberN: Integer
            Number to be returned
        string: str 
            The string in which to execute NGram Algorithm
    '''
    #for word in list
    

def getColors():
    """Load colors file into memory.

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

# Stores lenght of arguments passed
nLen = len(sys.argv)
# Check that lenght
nParamsCheck(nLen)
print("loading file... ", fileName())

print(getColors()["OKGREEN"])

print("WORDS FOUND IN FILE: \n")
print(getWords(fileName()))

exit()
