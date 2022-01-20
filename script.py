"""This module reads a filename, a number N and returns a N-Gram."""
import sys



'''
====================================
||                                ||
||  FUNCTION DEFINITIONS          ||
||                                ||
====================================
'''


def GetColors():
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
    print(GetColors()["OKCYAN"])
    print("""\n
        this script generates an N-gram given a filename \n
        and a number N between 0 and number of words in file \n
        usage: \n
            script.py filename n \n
            \n
            to print this statement use help, h or -h \n
        """)


def NParamsCheck(nLen):
    """Check script standard Input."""
    if nLen < 3:
        print(GetColors()["WHAT"])
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
NParamsCheck(nLen)
print("loading file... ", fileName())

exit()
