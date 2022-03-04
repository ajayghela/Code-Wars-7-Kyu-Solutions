#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

#Kata.getMiddle("test") should return "es"
#lenth of string
#figure out if length is odd or even
    #if even index is length/2 and (length+1)/2) - 1
    #if odd  index is (length+1)/2 - 1

def get_middle(s):
    x = len(s)
    if (x % 2) == 0:
        z = int(x/2)        
        w = int(z-1)
        return s[w] + s[z]
    else:
        y = int(((x+1)/2)-1)
        return (s[y])


