#Write a function that returns the sum of number of values associated #with a dictionary.

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''

    sum = 0
    for i in aDict.values():
        sum += len(i)
    return sum