##Assume s is a string of lower case characters.
##
##Write a program that prints the number of times the string 'bob' occurs in s.

count = 0
target = 'bob'

if target in s:
    index = s.index(target)
    string1 = s[index:len(target) + index]
    for position in range(0,len(s)):
        if s[position:len(target) + position] == string1:
            count += 1

print("Number of times bob occurs is: " + str(count))