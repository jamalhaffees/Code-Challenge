from pyparsing import Char


def only_ints(a,b):
    if type(a)==int and type(b)==int:
        return True
    return False

print (only_ints(2,4))
print (only_ints('c','d'))
print (only_ints('a',4))
print (only_ints(2,0.4))
print (only_ints(5,102))
