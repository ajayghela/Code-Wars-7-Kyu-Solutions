# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO() => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

s = "ooxx"
count_x = 0
count_o = 0
for i in list(s):
    if i == 'x':
        count_x += 1
    elif i == 'o':
        count_o += 1
print(count_o)
print(count_x)

x = s.lower()
return x.count('x') == x.count('o')