#sorted
def is_anagram1(text1, text2):
    return sorted(text1)== sorted(text2)

#comprehension, count, dictionary
def count_letters(text):
    return {letter: text.count(letter) for letter in text}

def is_anagram2(text1, text2):
    return count_letters(text1) == count_letters(text2)

print(is_anagram1('below', 'albow'))
print(is_anagram1('add', 'dad'))
print(is_anagram2('credit', 'debit'))
print(is_anagram2('match', 'catch'))