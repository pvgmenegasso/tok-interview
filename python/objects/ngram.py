'''
    This module implements object and function for Ngram calculation
'''

'''
====================================
||                                ||
||  CLASS DEFINITIONS             ||
||                                ||
====================================
'''

class Gram():
    '''

    '''
    def __init__(self, gram : str, count : int):
        
        self.__gram = gram 
        self.__count = count

    def getGram(self) -> str:
        return self.__gram

    def getCount(self) -> int:
        return self.__count


'''
====================================
||                                ||
||  FUNCTION DEFINITIONS          ||
||                                ||
====================================
'''

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
                nGram[gram] = value + 1
            # In case it's an inedit gram, insert it
            else:
                nGram[gram] = 1


    # Convert Dict to List for printing purposes
    nGramList : list[Gram] = []

    for key, value in nGram.items():
        gram = Gram(key, value)
        nGramList.append(gram)

    nGramList.sort(key = lambda x: x.getCount())

    # Finally return the N Grams
    return nGramList
