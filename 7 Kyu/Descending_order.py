#Your task is to make a function that can take any non-negative integer as an argument 
# and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.


def descending_order(num):
    lst = []
    number = str(num)   #turn num into a string
    for i in number:
        lst.append(i)   #make into a list
    order = sorted(lst, reverse=True)   #reverse the order
    n_order = ''.join(order)    #make the list into a string.
    return int(n_order)

    #return int("".join(sorted(str(num), reverse=True)))

    

