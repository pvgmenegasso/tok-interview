'''
This module reads a filename, a number N and returns a N-Gram.

Usage: python3 script.py filename N

'''
from fileinput import filename
from posixpath import split
import sys

from pyspark.sql import SparkSession

from pyspark.ml.feature import *

'''
====================================
||                                ||
||  FUNCTION DEFINITIONS          ||
||                                ||
====================================
'''

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

print("loading file... ")

filename = "../corpuses/grandeTexto.txt"

spark = SparkSession.builder.appName("spark").master("local[*]").getOrCreate()

textData = spark.createDataFrame(
    spark.sparkContext.textFile(filename).map(lambda x: x.split(' '))
)

textData.select('*').show()

ngram = NGram(n=3, inputCol="value")



# Change n-gram length

# Must use keyword arguments to specify params.



# Load color for aesthetic purposes
print(getColors()["OKGREEN"])

print('''
==========================================

        RESULTING N GRAM !!
        
-      -       -         -       -      -        -     -
''')



ngramresult = ngram.transform(textData.toLocalIterator())

ngramresult.head()

spark.stop()
exit()
