
# Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

string_ = "How can mirrors be real if our eyes aren't real"

upper_string = ''
for  i in string_.split():
    new = i[0].upper + i[1:]
    upper_string += new + ' '
print(upper_string.rstrip())

return " ".join(i[0].upper() + i[1:] for i in string_.split())
# .capwords from import string or .capialize
