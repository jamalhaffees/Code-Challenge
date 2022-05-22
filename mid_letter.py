def mid(text):
    if len(text) % 2 == 0:
        return ""
    return text[int(len(text)/2)]

print(mid("hello"))
print(mid("john"))
print(mid("aaaa"))