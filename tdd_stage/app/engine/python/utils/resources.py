

import json



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


def first_ele(lst: list, ref):

    '''
    gets the first value that is different from the reference value

    :param lst: list that will be analyzed
    :param ref: reference value that will serve the comparison process
    '''

    val = ref
    for i in lst:
        if i != ref:
            val = i
            break

    return val


def map_python_dtypes(vals_lst: list):

    '''
    establishes a parallel between python and sqlite datatypes
    
    :param vals_lst: list of values from where data types will be determined
    '''

    with open('./configs/python_dtypes.json', 'r') as f:
        py_dtypes = json.loads(f.read())  

    return [py_dtypes[type(v).__name__] for v in vals_lst]


def map_postsql_dtypes(types_lst: list):

    '''
    establishes a parallel between postgres and sqlite datatypes

    :param types_lst: list of postgresql data types to be converted
    '''

    with open('./configs/postsql_dtypes.json') as f:
        postsql_dtypes = json.loads(f.read())

    return [postsql_dtypes[t] for t in types_lst]


def get_pipeline_confs():

    '''
    extracts the configurations needed from the data pipeline
    '''

    with open('./configs/pipeline_config.json', 'r') as f:
        confs = json.loads(f.read())

    assets_map = confs['assets_map']
    data_nav = confs['data_navigator']
    key_cols = confs['key_columns']
    out_cols = confs['output_cols']

    return assets_map, data_nav, key_cols, out_cols


def check_outliers(ref_val, vals_set: list, idx: int):

    '''
    check if there is numbers different from the reference provided

    :param ref_val: reference value provided
    :param vals_set: set values that will be analyzed
    :param idx: specific positions to compare within the set of values
    '''

    has_outlier = False

    for val in vals_set:
        if val[idx] != ref_val:
            has_outlier = True
            break

    return has_outlier
