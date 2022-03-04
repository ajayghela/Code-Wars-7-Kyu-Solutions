# Description
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)


# arrange tuple so that the smallest value is first 
# return the sum of that range


def get_sum(a,b):
    if a > b:
        c = [b,a] #<---same as min(a,b) 
    else:
        c = [a,b] #<---same as max(a, b) 
    return sum(range(c[0], c[1] + 1))
    # return sum(range(min(a,b), max(a,b) + 1))

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

        

