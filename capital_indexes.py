def capital_indexes(text):
    final_list = []
    for order, letter in enumerate(text):
        if letter.isupper():final_list.append(order)
    return final_list

print(capital_indexes('HeLlO'))

shopping_list =['apple', 'orange', 'banana']
for order, fruit in enumerate(shopping_list):
    print(order,fruit)