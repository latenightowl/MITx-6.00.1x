##Assume s is a string of lower case characters.
##
##Write a program that counts up the number of vowels contained in the string s. 
##Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

count = 0
 
for vowel in s:
    if vowel in 'aeiou':
        count += 1

print("Number of vowels: " + str(count))