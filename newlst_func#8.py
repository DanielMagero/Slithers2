def new_list(lst1):
    return list(set(lst1))

lst1 = [1, 2, 3, 3, 3, 3, 4, 5]
print(new_list(lst1))