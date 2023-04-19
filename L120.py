#Krista, Rosemary, Olivia
def sort_dict_by_value(d):
    sorted_keys = sorted(d, key=d.get, reverse=True)
    return sorted_keys

my_dict = {"apple": 3, "banana": 2, "orange": 5, "pear": 1, "kiwi": 4}
my_list = sort_dict_by_value(my_dict)
print(my_list)
