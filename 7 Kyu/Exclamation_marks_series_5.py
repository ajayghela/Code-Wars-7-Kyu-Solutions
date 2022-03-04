#Description:
#Remove all exclamation marks from the end of words. Words are separated by spaces in the sentence.

#Examples
#remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi Hi"
# remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"

# split 
# rstrip('!') or reg ex
# concatenate back together
import re

s = "!!!Hi !!hi!!! !hi"
print(" ".join(x.rstrip("!") for x in s.split()))

def remove(s):
    final = ''
    for i in s.split():
        final +=  i.rstrip("!") + " "
    return final.rstrip()  