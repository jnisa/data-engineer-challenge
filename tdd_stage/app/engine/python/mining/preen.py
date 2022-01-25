


from collections import MutableMapping


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


def spot_jsonb(dtypes: list):

    '''
    lists all the indexes whose value has a jsonb data type

    :param dtypes: list of the data types from all the values
    '''

    return [idx for idx, val in enumerate(dtypes) if val == 'jsonb']


def unfold_jsonb(sch: list, cols: list, vals: list):

    '''
    targets the jsonb data types on the data and unfolds them in case 
    of a nested dictionary 
    
    :param sch: variable/list that handles the schema
    :param cols: variable/list that handles all the columns from the data
    :param vals: variable/list that handles all the data values
    '''


    jsonb_idxs = [spot_jsonb(subset) for subset in sch] 

    # 1. go record by record on the vals list
    # 2. iterate over the positions collected on the jsonb_idxs
    # 3. if the those positions are not None values store them in another list because
    # after unfolding the nested dicts they will be dropped
    # 4. unfold all the nested dicts and add them to the vals lst

    # ATTENTION we have to make sure that dicts columns have dict columns in all the records
    # That will come after testing the ElementsSelector

    return elems, dtypes, vals 

