#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

#Examples
#high_and_low("1 2 3 4 5")  # return "5 1"
#high_and_low("1 2 -3 4 5") # return "5 -3"
#high_and_low("1 9 3 4 -5") # return "9 -5"
#Notes
#All numbers are valid Int32, no need to validate them.
#There will always be at least one number in the input string.
#Output string must be two numbers separated by a single space, and highest number is first.

#def high_and_low(numbers):

#remove the spaces and use the min and max function

from os import X_OK


def high_and_low(numbers):
   lst = []
   x = numbers.split()  #removes the spaces
   for i in x:
       y = int(i)       #turn into int to use min and max functions
       lst.append(y)    #creates list of integers 
   high = max(lst)
   low = min(lst)
   return ' '.join([str(high),str(low)]) #remember square brackets

#def high_and_low(numbers):
    #l = [int(x) for x in numbers.split()]
    #return ' '.join([str(high),str(low)])