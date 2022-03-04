# Description:
# Move all exclamation marks to the end of the sentence

# Examples
# remove("Hi!") === "Hi!"
# remove("Hi! Hi!") === "Hi Hi!!"
# remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
# remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
# remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"

# Find total amount of exclamation marks in the string
# Remove all exclamations marks then add the total amount of exclamations marks back on.

def remove(s):
    return s.replace('!', '') + '!' * s.count('!')