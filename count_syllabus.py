def count_syllables1(text):
    return len(text.split('-'))

#using the count method
def count_syllables2(word):
    return word.count('-') + 1

print(count_syllables1('dic-ta-tor'))
print(count_syllables1('juggle'))
print(count_syllables2('ma-ra-th-on'))
print(count_syllables2('picture'))