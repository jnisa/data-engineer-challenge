

import pdb
from collections import MutableMapping

from tdd_stage.app.engine.python.crutches.auxiliars import first_ele
from tdd_stage.app.engine.python.crutches.auxiliars import map_python_dtypes


def preen(d: dict, parent_key = '', sep = '.'):

    '''
    preens python nested python dictionaries to erase existent nested levels 

    :param d: nested dictionary that is about to be unfolded
    '''

    items = []
    for k, v in d.items():
    
        new_key = parent_key + sep + k if parent_key else k
 
        if isinstance(v, MutableMapping):
            items.extend(preen(v, new_key, sep = sep).items())
    
        else:
            items.append((new_key, v))
    
    return dict(items)


def new_els_gen(parent: str, subels: list):

    '''
    generated new element ids based on the parent element and its predecessors
    
    :param parent: parent element to be subdivided
    :param subels: subelements resultant from the division
    '''

    return [parent + "." + s for s in subels]


def jsonb_conv(values: list, idx: int):

    '''
    convert the jsonb values into a python a dictionary

    :param values: set of values to be analyzed
    :param idx: value of the index that possesses jsonb data type variables
    '''

    unfold_function = lambda x : eval(x[idx].replace('null', 'None')) if x[idx] != None else (None)

    return unfold_function(values)


def adapt_feature(old_vals: list, new_vals: list, idx: int):

    '''
    adaption of the features after unfolding data entries

    :param old_vals: set of values to be updated
    :param new_vals: set of values that will be added to the old ones
    :param idx: index of where must occur the adaptation
    '''

    return old_vals[0:idx] + new_vals + old_vals[idx + 1::]


def unfold_jsonb(sch: list, cols: list, vals: list):

    '''
    targets the jsonb data types on the data and unfolds them in case 
    of a nested dictionary 
    
    :param sch: variable/list that handles the schema
    :param cols: variable/list that handles all the columns from the data
    :param vals: variable/list that handles all the data values
    '''

    pdb.set_trace()

    jsonb_idx = sch.index('jsonb')

    conv_values = [jsonb_conv(val, jsonb_idx) for val in vals]
    
    get_elements = lambda x: list(x.keys()) if x != None else (None)
    new_elements = first_ele([get_elements(val) for val in conv_values], None)
    
    get_values = lambda x: list(x.values()) if x != None else ([None] * len(new_elements))
    new_values = [get_values(val) for val in conv_values]

    elements = adapt_feature(cols, new_els_gen(cols[jsonb_idx], new_elements), jsonb_idx)
    schema = adapt_feature(sch, map_python_dtypes(first_ele(new_values, None)), jsonb_idx)    
    vals = [adapt_feature(vals[i], new_values[i], jsonb_idx) for i in range(len(vals))]

    pdb.set_trace()

    return schema, elements, vals




