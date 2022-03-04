# Description
# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Examples
# maskify("4556364607935616") == "############5616"
# maskify(     "64607935616") ==      "#######5616"
# maskify(               "1") ==                "1"
# maskify(                "") ==                 ""

# # "What was the name of your first pet?"
# maskify("Skippy")                                   == "##ippy"
# maskify("Nananananananananananananananana Batman!") == "####################################man!"

#  use the replace function
#  identify the last 4 digits using an 


num = "1"
y = len(num) - 4
z = num[-4:]
x = "".join(y*'#' + z)
print(x)

def maskify(cc):
    return "".join((len(cc) - 4)*'#' + cc[-4:])
