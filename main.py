# Write your function here
def combine_sort(lst1, lst2):
    new_list = lst1 + lst2
    new_list.sort()
    return new_list


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
