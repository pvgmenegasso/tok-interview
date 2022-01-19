import sys

'''Stores lenght of arguments passed'''
nLen = len(sys.argv)

'''
====================================
||                                ||
||  FUNCTION DEFINITIONS          ||
||                                ||
====================================
'''

def help():
    '''
        Prints help text
    '''
    print("\
        this script generates an N-gram given a filename and a number N between 0 and number of words in file\
        usage:\
        script.py filename n\
        \
        to print this statement use help, h or -h\
        ")



def nParamsCheck(nLen):
    '''
        If number of arguments is lesser than 3, then we are missing something !
        Remember that the first argument is always the name of the script itself
    '''
    if nLen < 3:
        print("missing arguments !")
        help()
        exit()
    elif sys.argv[1] == ("help" or "h" or "-h"):
        help()
        


def fileName():
    print("Input file: ", sys.argv[1])
    

# BEGIN

print("arrived")

nParamsCheck(nLen)




