#Your task is to write a function that takes a string and return a new string with all vowels removed.

#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

#def disemvowel(string_):
 #   return string_

string_ = "This website is for losers LOL!"

def disemvowel(string_):
    new = ''
    for i in string_:
        if i not in "aeiouAEIOU":   #only adds non vowels to the list
            new += i          #list of strings without vowels
        else:
            pass
    
    return new            #turns list back into a string

def disemvowel(string_):
    new = ''.join(i for i in string_ if i not in "aeiouAEIOU")
    return new

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")