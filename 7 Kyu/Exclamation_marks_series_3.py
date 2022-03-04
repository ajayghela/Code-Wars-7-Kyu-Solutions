#Decription:
#Remove all exclamation marks from sentence except at the end.

#Examples:
#remove("Hi!") == "Hi!"
#remove("Hi!!!") == "Hi!!!"
#remove("!Hi") == "Hi"
#remove("!Hi!") == "Hi!"
#remove("Hi! Hi!") == "Hi Hi!"
#remove("Hi") == "Hi"

#find out how many exclamation marks exsist at the end.
#remove all exclamation marks 
#add the exclamations marks back on.

import re
def remove(s):
    count = 0
    while s.endswith('!'):
        s = s[:-1]
        count += 1
    return s.replace('!', '') + '!' * count
 #  return re.sub(r'!+(?!!*$)', '', s)


s = "!Hi"
re.sub(r'^!*')