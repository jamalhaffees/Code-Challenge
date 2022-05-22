

def double_letters(text):
    for index in range(len(text)-1):
        if text[index]==text[index+1]: 
            return True
    return False

print(double_letters('Many'))
print(double_letters('Hello'))
print(double_letters('apple'))
print(double_letters('banana'))

#2
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])