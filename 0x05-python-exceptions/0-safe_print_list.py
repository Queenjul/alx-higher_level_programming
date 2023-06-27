#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list '''
    try:
        tmp = 0
        while tmp < x:
            print("{}".format(my_list[tmp]), end='')
            tmp += 1
        print()
        return tmp
    except IndexError:
        print()
        return tmp
    pass
