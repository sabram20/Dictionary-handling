ex_dict = {"key1": 31, "key2": 45, "key3": 72, "key4": 15}
min = min(zip(ex_dict.values(), ex_dict.keys()))
max = max(zip(ex_dict.values(), ex_dict.keys()))
print(min)
print(max)