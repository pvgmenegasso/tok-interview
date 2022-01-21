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
    
    '''Return Words in a file in form of a list of strings.'''
    
    # String to store results
    result : [str] = []
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



def nGram(listOfWords: list[str], numberN: int):
    
    '''
    
    Given a number N return a Ngram from a given a list of words
    
    @PARAMS:
        numberN: Integer
            Weight of the gram, 1-gram, 2-gram etc...
        string: str 
            Words extracted from the file, to use the algorithm on
            
    @RETURNS:
        nGram: dict
            The resulting N-Gram
            
    '''
    
    # A dictionary seems like a smart way to save the results !
    nGram: dict[str, int] = {}

    # Loop through the main list of words
    for index, word in enumerate(listOfWords):
        # Check if index + N does not result in access out of range
        if index+numberN <= len(listOfWords):
            # Define variable to store the current "gram"
            gram = ''
            
            # Loop through the first N words of the index
            for i in range(0, numberN):
                # Append to the gram
                gram = gram+listOfWords[index+i]+' '
            # If it's not a new gram, add to it's value
            if gram in nGram:
                # Get count value
                value = nGram[gram]
                # Update it
                nGram[gram] = value+1
            # In case it's an inedit gram, insert it
            else:
                nGram[gram] = 1
    
    # Finally return the N Gram
    return nGram



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

# Prints all words found on the file
print('''
======================================================
      
      WORDS FOUND IN FILE :
          

-     -      -      -      -      -      -      -    -      
''')

words = getWords(fileName())
print(words)


print('''
==========================================

        RESULTING N GRAM !!
        
-      -       -         -       -      -        -     -
''')

gramN = nGram(words, int(sys.argv[2]))
print(gramN)

exit()
