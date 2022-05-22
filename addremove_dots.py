def add_dots(text):
    return '.'.join(text)

#replace
def remove_dots(text):
    return text.replace('.', '')

print(remove_dots(add_dots('Hello. How. are. you')))
print(remove_dots(add_dots('world!')))
print(add_dots(remove_dots('ABCDEFG')))