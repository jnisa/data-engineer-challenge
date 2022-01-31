


from collections import Iterable
from collections import MutableMapping

from tdd_stage.app.engine.python.utils.resources import first_ele
from tdd_stage.app.engine.python.utils.resources import check_outliers
from tdd_stage.app.engine.python.utils.resources import map_python_dtypes



def circumvent(data: dict, keys=None):
    
    '''
    dribbler that retrieves elements from a nested dictionary

    :param data: playground for the dribbler
    :param keys: pin points that the dribbler must follow
    '''
    
    result = []
    
    if isinstance(data, dict):
        if keys is None:
            data = data.values()
        else:
            data = dict(filter(lambda t: t[0] in keys, data.items())).values()
    
    for el in data:
        if isinstance(el, Iterable) and not isinstance(el, str):
            result.extend(circumvent(el, keys))
        else:
            result.append(el)
    
    return result


def collier(raw_data: dict, dims: int, map: dict, keys: list):

    '''
    gets all the needed assets from the json file
    returns lists with the data types, columns, records values, and dims name

    :param raw_data: data from the initial json
    :param dims: data dimensions
    :param map: position of each data asset 
    :param keys: pin points to navigate in the nested dictionary
    '''

    values = [[] for _ in range(dims)]
    dtypes = [None for _ in range(dims)]
    columns = [None for _ in range(dims)]

    for r in raw_data:
        
        idx = map[circumvent(r, keys[0])[0]]
        values[idx].append(circumvent(r, keys[1]))

        if (None in dtypes or dtypes[idx] == None):

            dtypes[idx] = circumvent(r, keys[2])
            columns[idx] = circumvent(r, keys[3])

    return dtypes, columns, values


def preen(d: dict, parent_key = '', sep = '.'):

    '''
    preens python nested python dictionaries to erase existent nested levels 

    :param d: nested dictionary that is about to be unfolded
    :param parent_key: corresponds to the name of dimensions
    :param sep: separator that stays in between the dimension and the column name
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

    return [parent + "_" + s for s in subels]


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

    if 'jsonb' in sch:
        if check_outliers(None, vals, sch.index('jsonb')):
            jsonb_idx = sch.index('jsonb')

            conv_values = [jsonb_conv(val, jsonb_idx) for val in vals]
            
            get_elements = lambda x: list(x.keys()) if x != None else (None)
            new_elements = first_ele([get_elements(val) for val in conv_values], None)
            
            get_values = lambda x: list(x.values()) if x != None else ([None] * len(new_elements))
            new_values = [get_values(val) for val in conv_values]

            #cols = adapt_feature(cols, new_els_gen(cols[jsonb_idx], new_elements), jsonb_idx)
            cols = adapt_feature(cols, new_elements, jsonb_idx)
            sch = adapt_feature(sch, map_python_dtypes(first_ele(new_values, None)), jsonb_idx)   
            vals = [adapt_feature(vals[i], new_values[i], jsonb_idx) for i in range(len(vals))]

    return sch, cols, vals




