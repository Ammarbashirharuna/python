from pprint import pprint
#finding the most repeated character
character = "Thi is the most common interview question"
char_prequency = {}
for char in character:
    if char in char_prequency:
        char_prequency[char] += 1
    else:
        char_prequency[char] = 1
# pprint(char_prequency, width=1)
sorting_item = sorted(char_prequency.items(),
 key=lambda kv:kv[1],
 reverse=True)
print(sorting_item[0])










