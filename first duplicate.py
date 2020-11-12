list = [1, 2, 4, 3, 5, 2]

def get_first_duplicate(list):
    new_list = []
    if len(set(list)) != len(list):
        for i in list:
            if i in new_list:
                return i
            new_list.append(i)

    else:
        return 'there is no duplicates'

print(get_first_duplicate(list))