#An isogram is a word that has no repeating letters,consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.


def is_isogram(string):
    #data structure to remember the letters
    output = []

    str = string.lower()  #convert to lower case
    
    # iterate through each elelment 
    for character in str:
        if not character.isalpha():  #Check it is part of the alphabet and not numbers
            continue
        if character in output:
            return False
        else:
            output.append(character)
    return True
    
# A better way https://stackoverflow.com/questions/37924869/check-python-function-determine-isogram-from-codewars:

def is_isogram(string):
    s = string.lower()
    return len(set(s)) == len(s)


