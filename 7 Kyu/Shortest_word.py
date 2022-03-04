# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# set the smallet to the length of the first element in the list after it's been split
# then traverse through the elements replacing the smallest when a smaller length is found.
# or use min function

string_ = "bitcoin take over the world maybe who knows perhaps"
def find_short(s):
      
    smallest_length = len(string_.split()[0])
    for i in string_.split():
        if len(i) < smallest_length:
            smallest_length = len(i)
    return smallest_length



    # return min(len(x) for x in s.split()) <-- using min function.
