#Make a program that filters a list of strings and returns a list with only your friends name in it.

#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

#Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

#go throught list
#for indivual word if the length is 4 characters add to a new a list.
#retrun new list of words

def friend(x):
    new_lst = []
    for word in x:
        if len(word) == 4:
            new_lst.append(word)
    return new_lst

    #return[i for i in x if len(i) == 4]