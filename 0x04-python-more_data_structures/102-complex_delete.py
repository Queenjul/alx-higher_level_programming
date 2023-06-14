#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''Deletes keys with a specific value in a dictionary.'''
    while value in a_dictionary.values():
        for j, i in a_dictionary.items():
            if i == value:
                del a_dictionary[j]
                break
    return (a_dictionary)
