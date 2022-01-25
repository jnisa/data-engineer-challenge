


from tdd_stage.app.engine.python.navigator.circumvent import circumvent


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