# Description
#  In this kata you will create a function that takes a list of non-negative 
#  integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# Check each element to check it's not a string, appending those that are to a new list

s = [1,2,'aasf','1','123', 123]
new_s = []
for i in s:
    if type(i) != str:
       new_s.append(i)

print(new_s)
# new_s = []
# return [i for i in s if type(i) == int]
# return [i for i in s if type(x) != str]