# Description
# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

s = "ZpglnRxqenU"
i = 0
final = ''
for letter in s:
    final += letter.upper() + letter.lower()*i + '-'
    i += 1
print(final[:-1])

def accum(s):
    return '-'.join(str(i*s).title() for s,i in enumerate(s, 1))
    return '-'.join(i.upper() + i.lower() * c for c, i in enumerate(s))
