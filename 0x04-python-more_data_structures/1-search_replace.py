#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list = []
    for item in my_list:
        if item == search:
            my_list.append(replace)
        else:
            my_list.append(item)
    return my_list
