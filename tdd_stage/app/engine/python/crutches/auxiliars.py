


def clean_up(vals: list, del_pos: list):

    '''
    takes down all the useless positions of data assets
    
    :param vals: set of valus that will be filtered
    :param del_pos: indexes of the values that will be erased
    '''

    for index in sorted(del_pos, reverse=True):
        del vals[index]

    return vals


def nested_levls_counter(lst: list):

    '''
    counts the number of nested lists from a provided python list

    :param lst: input list to be evaluated
    '''

    f = lambda lst: 0 if not isinstance(lst,list) else (f(lst[0]) + f(lst[1:]) if len(lst) else 1)
    return f(lst) - 1