#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

#Note: The function accepts an integer and returns an integer
#turn into a string
#iterate through the string
#take each element turn it into a integer and square it 
#then turn back into a string and add to sqr 
#convert to an integer

def square_digits(num):
    sqr = ""
    for i in str(num):
        x = int(i)**2
        sqr += str(x)
    return int(sqr)

#more versions:

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

def square_digits(num):
    return int(''.join(str(int(c)**2) for c in str(num)))