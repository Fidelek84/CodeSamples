my_number_of_path = [1, 1, 1, 1, 1, 1, 1, 2, 1, 4, 2]

my_multipath_list = []

for paths in my_number_of_path:
    if paths > 1:
        my_multipath_list.append(paths)
        print(my_multipath_list)