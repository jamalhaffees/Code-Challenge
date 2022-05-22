# from itertools import count


# statuses = {
#     "Alice": "online",
#     "Jessy": "online",
#     "Maddy": "offline",
#     "Mike": "online",
#     "Abbas": "offline"
# }

# def online_count(statuses):
#     counter = 0
#     for status in statuses.values():
#         if status == "online": counter += 1
#     return counter

# print(online_count(statuses))

# #2 
# def online_count(people):
#     count = 0
#     for person, status in people.items():
#         if status == "online":
#             count += 1
#     return count

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])
