#Using recursion and bisection search, determine if a character
#is in a string, so long as the string is sorted in alphabetical
#order.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    x: the first test character
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr == char
    if char == aStr[len(aStr)//2]:
        return True
    elif char > aStr[len(aStr)//2]:
        return isIn(char, aStr[len(aStr)//2+1:])
    else:
        return isIn(char, aStr[:len(aStr)//2])
        