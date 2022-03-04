# Description:
# Remove words from the sentence if it contains one exclamation mark. 
# Words are separated by spaces in the sentence. Please remember, one.

# Examples
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# count exclamation marks in each part 
# if equal to 1 miss

import re
s = "Hi! !Hi Hi!"
fin = ''
y = s.split()
for i in y:
    if i.count('!') != 1:
        fin += i + " "
    print(fin.rstrip())

print(''.join(i for i in s.split() if i.count('!') != 1))
