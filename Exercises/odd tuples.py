#Write a function which takes a tuple as input and returns a new
#tuple as out, where every other element of the input tuple is copied.

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for x in aTup[0::2]:
        newTup = newTup + (x,)
    return (newTup)
