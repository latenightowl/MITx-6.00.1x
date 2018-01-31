#Write a function that returns the key corresponding to the entry with the largest number of values associated with it.

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = None
    max = 0
    for i in aDict.keys():
        if len(aDict[i]) >= max:
            max = len(aDict[i])
            result = i
    return result
