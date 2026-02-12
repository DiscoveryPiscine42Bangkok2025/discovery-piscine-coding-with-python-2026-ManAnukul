#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []
seen = set()

for number in original_array:
    if number > 5:
        value = number + 2
        if value not in seen:
            new_array.append(value)
            seen.add(value)

print(original_array)
print(new_array)
