


def clean_up(vals: list, del_pos: list):

    '''
    takes down all the useless positions of data assets
    
    :param vals: set of valus that will be filtered
    :param del_pos: indexes of the values that will be erased
    '''

    for index in sorted(del_pos, reverse=True):
        del vals[index]

    return vals