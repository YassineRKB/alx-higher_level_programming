#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = list()
    for i in range(len(my_list)):
        if i != search:
            newList.append(i)
        else:
            newList.append(replace)
    return newList

