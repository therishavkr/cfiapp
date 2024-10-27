nested_array = [1, [2, [3, [4, 5]], 6], 7]

new_list = []
stack = nested_array.copy()

while stack:
    current = stack.pop()
    if isinstance(current, list):
        stack.extend(current)
    else:
        new_list.append(current)

final_list = []
index = len(new_list) - 1

while index >= 0:
    final_list.append(new_list[index])
    index -= 1

print(final_list)

