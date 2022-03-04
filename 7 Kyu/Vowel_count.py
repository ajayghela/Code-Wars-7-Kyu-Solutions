#Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.

#go trhough the string and check for a, if present at 1 to count
#repeat for all other e,i,o,u

input = 'rabbit'
count = 0
for i in input:
    if 'a' == i:
        count +=1
    if 'e' == i:
        count +=1
    if 'i' == i:
        count +=1
    if 'o' == i:
        count +=1
    if 'u' == i:
        count +=1
    return count


def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels