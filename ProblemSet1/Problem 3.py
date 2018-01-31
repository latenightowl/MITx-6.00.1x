##Assume s is a string of lower case characters.
##
##Write a program that prints the longest substring of s in which the ##letters occur in alphabetical order.
##
##In the case of ties, print the first substring.

max = 0
str1 = s[0]
str2 = s[0]
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        str1 += s[i + 1]
        if len(str1) > max:
            max = len(str1)
            str2 = str1
    else:
        str1=s[i + 1]
    i += 1
print("Longest substring in alphabetical order is: "" + str2)