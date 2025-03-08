def get_list_dimension(lst):
    if not isinstance(lst, list):
        return 0
    sub_list = lst[0]
    return 1 + get_list_dimension(sub_list)

my_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(get_list_dimension(my_list))