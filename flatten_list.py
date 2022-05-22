def flatten(list_of_lists):
    new_list = []
    for sub_list in list_of_lists: new_list.extend(sub_list)
    return new_list

print(flatten([[1,2],[3,4]]))
print(flatten([[1,2],[3,4], [5,6]]))