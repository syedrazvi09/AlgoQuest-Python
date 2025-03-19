list_a = [2, 4, 5, 6, 5, 1, 4, 7]
list_c = [2, 4, 5, 8, 5, 1, 4, 9]

set_b = set(list_a)
set_d = set(list_c)

print("List A:", list_a)
print("List C:", list_c)

print("Set B:", set_b)
print("Set D:", set_d)

union_result = set_b | set_d
print("Union of Set B and Set D:", union_result)
